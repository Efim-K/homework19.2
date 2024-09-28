from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, UserChangeForm
from django import forms

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Форма регистрации пользователя"""

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class ResetPasswordForm(StyleFormMixin, PasswordResetForm):
    """Форма для сброса пароля"""

    class Meta:
        model = User
        fields = ['email', ]


class UserProfileForm(StyleFormMixin, UserChangeForm):
    """Форма редактирования профиля пользователя"""

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'avatar', 'country', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
