from django import forms
from .models import Department, FeeRecord, Grade
from accounts.models import Student


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name", "description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["standard", "section", "in_charge"]
        widgets = {
            "in_charge": forms.Select(attrs={"class": "form-select"}),
        }


class FeeRecordForm(forms.ModelForm):
    class Meta:
        model = FeeRecord
        fields = ["grade", "student", "amount", "due_date", "remarks"]
        widgets = {"due_date": forms.DateInput(attrs={"type": "date"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["student"].queryset = Student.objects.none()

        if "grade" in self.data:
            grade_id = int(self.data.get("grade"))
            self.fields["student"].queryset = Student.objects.filter(grade_id=grade_id)
        elif self.instance.pk:
            self.fields["student"].queryset = Student.objects.filter(
                grade=self.instance.grade
            )
