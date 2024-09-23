from django.db import models
from django.contrib.auth.models import AbstractUser

from catalog.models import NULLABLE


# Create your models here.
class User(AbstractUser):
    """
    Пользователь с полями почта, аватар, телефон, страна
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to="users/avatars", verbose_name="Аватар", **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Phone', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Country', **NULLABLE)

    token = models.CharField(max_length=100, verbose_name='Token', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
