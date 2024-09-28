from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

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
        fields = ['email',]
