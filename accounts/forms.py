from django import forms
from .models import Department, Admin, Staff, Librarian


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
            "profile_photo",
            "emergency_contact",
            "department",
            "qualification",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "address": forms.Textarea(attrs={"rows": 3}),
        }
        help_texts = {
            "username": "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
            "email": "Required. Enter a valid email address.",
        }


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
            "profile_photo",
            "emergency_contact",
            "department",
            "designation",
            "qualification",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "address": forms.Textarea(attrs={"rows": 3}),
        }
        help_texts = {
            "username": "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
            "email": "Required. Enter a valid email address.",
        }


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
            "profile_photo",
            "emergency_contact",
            "qualification",
            "joining_date",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "joining_date": forms.DateInput(attrs={"type": "date"}),
            "address": forms.Textarea(attrs={"rows": 3}),
        }
        help_texts = {
            "username": "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
            "email": "Required. Enter a valid email address.",
        }
