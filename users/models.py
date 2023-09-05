from django.contrib.auth.models import AbstractUser
from django.db import models

from habbits.models import NULLABLE, NOT_NULLABLE


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='Эмайл пользователя')
    chat_id = models.IntegerField(unique=True, **NULLABLE, default=None)
    telegram_user_name = models.CharField(max_length=150, **NOT_NULLABLE, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
