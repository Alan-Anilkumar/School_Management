from django import forms
from accounts.models import Student
from .models import LibraryRecord, Book


class LibraryRecordForm(forms.ModelForm):
    class Meta:
        model = LibraryRecord
        fields = ["grade", "student", "book", "borrowed_date", "due_date", "remarks"]
        widgets = {
            "borrowed_date": forms.DateInput(attrs={"type": "date"}),
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "grade" in self.data:
            grade_id = int(self.data.get("grade"))
            self.fields["student"].queryset = Student.objects.filter(
                grade_id=grade_id
            )
        elif self.instance.pk:
            self.fields["student"].queryset = Student.objects.filter(
                grade=self.instance.grade
            )
        else:
            # Show all students if no grade is selected
            self.fields["student"].queryset = Student.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        borrowed_date = cleaned_data.get("borrowed_date")
        due_date = cleaned_data.get("due_date")

        if borrowed_date and due_date and borrowed_date > due_date:
            self.add_error("due_date", "Due date cannot be before borrowed date.")


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "total_copies", "available_copies"]

        # Optional: Add widgets for better UI control
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "total_copies": forms.NumberInput(attrs={"class": "form-control"}),
            "available_copies": forms.NumberInput(attrs={"class": "form-control"}),
        }
