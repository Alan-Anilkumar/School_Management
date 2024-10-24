from django import forms
from accounts.models import Student
from .models import LibraryRecord, Book


class LibraryRecordForm(forms.ModelForm):
    class Meta:
        model = LibraryRecord
        fields = [
            "grade",
            "student",
            "book",
            "borrowed_date",
            "due_date",
            "return_date",
            "remarks",
        ]
        widgets = {
            "grade": forms.Select(attrs={"class": "form-control"}),
            "student": forms.Select(attrs={"class": "form-control"}),
            "book": forms.Select(attrs={"class": "form-control"}),
            "borrowed_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "due_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "return_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "remarks": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and not self.instance.pk:
            self.fields.pop('return_date', None)
        else:
            self.fields['return_date'].widget.attrs.pop('disabled', None)

    def clean_due_date(self):
        borrowed_date = self.cleaned_data.get("borrowed_date")
        due_date = self.cleaned_data.get("due_date")

        if due_date and due_date < borrowed_date:
            raise forms.ValidationError(
                "Due date cannot be earlier than borrowed date."
            )
        return due_date

    def clean_return_date(self):
        return_date = self.cleaned_data.get("return_date")
        status = self.cleaned_data.get("status")

        if status == "RETURNED" and not return_date:
            raise forms.ValidationError(
                "Return date is required when status is Returned."
            )
        return return_date


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
