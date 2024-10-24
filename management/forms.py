from django import forms
from .models import Department, FeeRecord, Grade
from accounts.models import Student


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Department name"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 2,
                }
            ),
        }


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["standard", "section", "in_charge"]
        widgets = {
            "standard": forms.NumberInput(attrs={"class": "form-control"}),
            "section": forms.TextInput(attrs={"class": "form-control"}),
            "in_charge": forms.Select(attrs={"class": "form-select"}),
        }


class FeeRecordForm(forms.ModelForm):
    class Meta:
        model = FeeRecord
        fields = [
            "grade",
            "student",
            "amount",
            "due_date",
            "payment_date",
            "status",
            "remarks",
        ]
        widgets = {
            "due_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "payment_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "amount": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter the amount"}),
            "grade": forms.Select(attrs={"class": "form-select"}),
            "student": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("grade" in self.data)

        if self.instance.pk:
            # If editing existing record, show students from the selected grade
            self.fields["student"].queryset = Student.objects.filter(
                grade=self.instance.grade
            ).order_by("first_name", "last_name")
        elif "grade" in self.initial:
            # Handle GET request or initial display when grade is pre-populated
            grade_id = self.initial.get("grade")
            self.fields["student"].queryset = Student.objects.filter(
                grade_id=grade_id
            ).order_by("first_name", "last_name")
        else:
            # Initially or if no grade selected, show no students
            self.fields["student"].queryset = Student.objects.all()

        # Override the student display format
        for student in self.fields["student"].queryset:
            student.display_name = (
                f"{student.first_name} {student.last_name} ({student.registration_id})"
            )

    def clean_payment_date(self):
        payment_date = self.cleaned_data.get("payment_date")
        status = self.cleaned_data.get("status")

        if status == "PAID" and not payment_date:
            raise forms.ValidationError("Payment date is required when status is Paid")
        return payment_date
