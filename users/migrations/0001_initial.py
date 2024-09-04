# Generated by Django 5.1 on 2024-09-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField()),
                ('phone_number', models.CharField(blank=True, max_length=25, null=True)),
                ('address', models.TextField()),
                ('avatar', models.ImageField(upload_to='')),
                ('birth_date', models.DateField()),
                ('date_joined_at', models.DateTimeField(auto_now_add=True)),
                ('is_superuser', models.BooleanField()),
                ('is_staff', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
