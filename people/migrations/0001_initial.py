# Generated by Django 4.2.7 on 2024-01-25 00:47

from django.db import migrations, models
import django.db.models.deletion
import people.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('middlename', models.CharField(max_length=100, verbose_name='Отчество')),
                ('biography', models.TextField(verbose_name='Биография')),
                ('image', models.ImageField(upload_to=people.models.Person.upload_to, verbose_name='Основное фото')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
            },
        ),
        migrations.CreateModel(
            name='PersonCategorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название категории')),
                ('sorting', models.IntegerField(verbose_name='Сортировка')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('has_self_page', models.BooleanField(default=True, verbose_name='Есть собственная страница')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='PersonImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=people.models.PersonImage.upload_to, verbose_name='Фото')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.person', verbose_name='Актёр')),
            ],
            options={
                'verbose_name': 'Изображение человека',
                'verbose_name_plural': 'Изображения людей',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.position', verbose_name='Должность'),
        ),
    ]
