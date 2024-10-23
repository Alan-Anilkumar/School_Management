from django import forms
from accounts.models import Student
from .models import LibraryRecord


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
        # Initially disable student dropdown until grade is selected
        self.fields["student"].queryset = Student.objects.none()

        # If form is being edited and already has grade selected
        if "grade" in self.data:
            try:
                grade_id = int(self.data.get("grade"))
                self.fields["student"].queryset = Student.objects.filter(
                    grade_id=grade_id
                )
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields["student"].queryset = Student.objects.filter(
                grade=self.instance.grade
            )
