from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm

from apps.accounts.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Логін",
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class":"form-control"}
        )
    )
    password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "birthday",
        ]
        form_control = {"class": "form-control"}
        widgets={
            "username": forms.TextInput(attrs=form_control),
            "first_name": forms.TextInput(attrs=form_control),
            "last_name": forms.TextInput(attrs=form_control),
            "email": forms.EmailInput(attrs=form_control),
            "phone": forms.TextInput(attrs=form_control),
            "birthday": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "avatar",
            "email",
            "first_name",
            "last_name",
            "birthday",
            "phone",
            "is_private",
        ]
        form_control = {"class": "form-control"}
        widgets={
            "avatar": forms.FileInput(attrs=form_control),
            "email": forms.EmailInput(attrs=form_control),
            "first_name": forms.TextInput(attrs=form_control),
            "last_name": forms.TextInput(attrs=form_control),
            "phone": forms.TextInput(attrs=form_control),
            "birthday": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),
            "is_private": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            )
        }


class UserPasswordChangeForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ["new_password1", "new_password2"]
