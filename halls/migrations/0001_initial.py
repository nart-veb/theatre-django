# Generated by Django 4.2.7 on 2024-01-25 00:47

from django.db import migrations, models
import django.db.models.deletion
import halls.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название зала')),
                ('descrpition', models.TextField(verbose_name='Описание зала')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
            },
        ),
        migrations.CreateModel(
            name='HallImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=halls.models.HallImage.upload_to, verbose_name='Изображение зала')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='halls.hall', verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Изображение зала',
                'verbose_name_plural': 'Изображения залов',
            },
        ),
    ]
