from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import ClientProfile


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ClientProfile
        fields = ['bio', 'birth_date', 'phone_number', 'address', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        max_length=100,
        widget=forms.CharField,
    )
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput,
    )

    error_messages = {
        'invalid_login': "Пожалуйста, введите правильные имя пользователя и пароль. "
                         "Обратите внимание, что оба поля могут быть чувствительны к регистру.",
    }
