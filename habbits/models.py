import django
from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}
NOT_NULLABLE = {'null': False, 'blank': False}


class Hobbit(models.Model):
    class Frequency(models.TextChoices):
        pass

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name="Владелец привычки")
    place = models.CharField(max_length=150, **NOT_NULLABLE, verbose_name='Место привычки')
    time = models.TimeField(default=django.utils.timezone.now, verbose_name='Время привычки')
    action = models.CharField(max_length=150, **NOT_NULLABLE, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Приятная привычка')
    link_pleasant = models.ForeignKey("self", on_delete=models.CASCADE, **NULLABLE)
    frequency = models.CharField(choices=Frequency.choices, default=Frequency.Daily)
    award = models.CharField(max_length=150, **NULLABLE, verbose_name='Награда')
    duration = models.IntegerField(**NOT_NULLABLE, verbose_name='Продолжительность привычки')
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f"Действие: {self.action} Место: {self.place}"

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
