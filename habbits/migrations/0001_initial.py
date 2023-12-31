# Generated by Django 4.2.3 on 2023-09-05 18:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobbit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=150, verbose_name='Место привычки')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='Время привычки')),
                ('action', models.CharField(max_length=150, verbose_name='Действие')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='Приятная привычка')),
                ('frequency', models.CharField(choices=[('ЕЖЕДНЕВНО', 'Daily'), ('ПОНЕДЕЛЬНИК', 'Monday'), ('ВТОРНИК', 'Tuesday'), ('СРЕДА', 'Wednesday'), ('ЧЕТВЕРГ', 'Thursday'), ('ПЯТНИЦА', 'Friday'), ('СУББОТА', 'Saturday'), ('ВОСКРЕСЕНЬЕ', 'Sunday')], default='ЕЖЕДНЕВНО')),
                ('award', models.CharField(blank=True, max_length=150, null=True, verbose_name='Награда')),
                ('duration', models.IntegerField(verbose_name='Продолжительность привычки')),
                ('is_public', models.BooleanField(default=True)),
                ('link_pleasant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habbits.hobbit')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
