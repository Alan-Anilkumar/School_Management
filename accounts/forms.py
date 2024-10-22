from django import forms
from accounts.models import Admin, Staff, Librarian, Student
from django.forms.widgets import DateInput
from management.models import Department, FeeRecord
from library.models import LibraryRecord


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name", "description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }


class BaseCustomUserForm(forms.ModelForm):
    """
    Base form incorporating features from both UserCreationForm and UserChangeForm
    """

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        required=False,
        help_text="Leave empty if not changing password.",
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        required=False,
        help_text="Enter the same password as above, for verification.",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # New user
            self.fields["password1"].required = True
            self.fields["password2"].required = True
            self.fields["password1"].help_text = "Required. Enter a strong password."

        # Make all fields required=False for updates
        if self.instance.pk:
            for field in self.fields.values():
                field.required = False

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 or password2:  # If either password field is filled
            if password1 != password2:
                raise forms.ValidationError("Passwords don't match")
            if len(password1) < 8:
                raise forms.ValidationError(
                    "Password must be at least 8 characters long"
                )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get("password1"):
            user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AdminForm(BaseCustomUserForm):
    class Meta:
        model = Admin
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "date_of_birth",
            "gender",
            "profile_picture",
            "emergency_contact",
            "department",
            "qualification",
        ]
        widgets = {
            "department": forms.Select(attrs={"class": "form-select"}),
            "gender": forms.Select(attrs={"class": "form-select"}),
            "date_of_birth": DateInput(attrs={"class": "form-control", "type": "date"}),
            "profile_picture": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "qualification": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your username"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter your email"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your first name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your last name"}
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your phone number",
                }
            ),
            "emergency_contact": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your phone number",
                }
            ),
        }

    address = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 2,
                "placeholder": "Enter your address",
            }
        ),
    )

    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get("profile_picture")
        if profile_picture:
            return profile_picture
        return self.instance.profile_picture


class StaffForm(BaseCustomUserForm):
    class Meta:
        model = Staff
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "date_of_birth",
            "gender",
            "profile_picture",
            "emergency_contact",
            "department",
            "qualification",
        ]
        widgets = {
            "department": forms.Select(attrs={"class": "form-select"}),
            "gender": forms.Select(attrs={"class": "form-select"}),
            "date_of_birth": DateInput(attrs={"class": "form-control", "type": "date"}),
            "profile_picture": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "qualification": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your username"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter your email"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your first name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your last name"}
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your phone number",
                }
            ),
            "emergency_contact": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your phone number",
                }
            ),
        }

    address = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 2,
                "placeholder": "Enter your address",
            }
        ),
    )


class LibrarianForm(BaseCustomUserForm):
    class Meta:
        model = Librarian
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "date_of_birth",
            "gender",
            "profile_picture",
            "emergency_contact",
            "qualification",
            "joining_date",
        ]
        widgets = {
            "gender": forms.Select(attrs={"class": "form-select"}),
            "date_of_birth": DateInput(attrs={"class": "form-control", "type": "date"}),
            "joining_date": DateInput(attrs={"class": "form-control", "type": "date"}),
            "profile_picture": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "qualification": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your username"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter your email"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your first name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your last name"}
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your phone number",
                }
            ),
            "emergency_contact": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your phone number",
                }
            ),
        }

    address = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 2,
                "placeholder": "Enter your address",
            }
        ),
    )


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


class FeeRecordForm(forms.ModelForm):
    class Meta:
        model = FeeRecord
        fields = ["grade", "student", "amount", "due_date", "remarks"]
        widgets = {"due_date": forms.DateInput(attrs={"type": "date"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["student"].queryset = Student.objects.none()

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
