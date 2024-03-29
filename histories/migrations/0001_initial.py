# Generated by Django 4.2.7 on 2024-01-25 00:47

from django.db import migrations, models
import histories.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название периода')),
                ('start_period', models.PositiveIntegerField(verbose_name='Год начала периода')),
                ('end_period', models.PositiveIntegerField(verbose_name='Год окончания периода')),
                ('image', models.ImageField(upload_to=histories.models.History.upload_to, verbose_name='Изображение')),
                ('text', models.TextField(verbose_name='Описание периода')),
            ],
            options={
                'verbose_name': 'История',
                'verbose_name_plural': 'Истории',
            },
        ),
    ]
