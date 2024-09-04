from django.db import models


class User(models.Model):
    """Модель для пользователей"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)
    password = models.TextField()

    phone_number = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )
    address = models.TextField()
    avatar = models.ImageField()

    birth_date = models.DateField()
    date_joined_at = models.DateTimeField(auto_now_add=True)

    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
