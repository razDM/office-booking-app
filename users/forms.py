from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html

AuthUserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = AuthUserModel
        fields = ['first_name', 'last_name', 'username']
