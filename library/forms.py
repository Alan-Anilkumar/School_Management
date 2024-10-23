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
        # Initially disable the student field until grade is selected
        self.fields["student"].queryset = Student.objects.none()
        self.fields["student"].widget.attrs.update(
            {"disabled": "true"}
        )  # Disable student field initially

        # If grade is selected via POST request or editing a record
        if "grade" in self.data:
            grade_id = int(self.data.get("grade"))
            self.fields["student"].queryset = Student.objects.filter(grade_id=grade_id)
            self.fields["student"].widget.attrs.pop(
                "disabled", None
            )  # Enable student field if grade is selected
        elif self.instance.pk:
            # When editing an existing record, set the student queryset to the current grade
            self.fields["student"].queryset = Student.objects.filter(
                grade=self.instance.grade
            )
            self.fields["student"].widget.attrs.pop(
                "disabled", None
            )  # Enable field when editing

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
