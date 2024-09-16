from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import CustomUser


class ProductCategory(models.Model):
    """Модель для категории товара"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Product(models.Model):
    """Модель товара"""

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)

    price = models.PositiveIntegerField(verbose_name='цена', help_text='в сомах')
    sales_percent = models.PositiveSmallIntegerField(
        verbose_name='скидка в процентах',
        blank=True,
        validators=[MaxValueValidator(100)]
    )

    description = models.TextField()
    preview_image = models.ImageField(upload_to='product preview images')

    new_expiry_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def get_price_with_sales(self):
        """Возвращает цену с учётом скидки"""
        if self.sales_percent == 0:
            return self.price
        else:
            return int((self.price / 100) * (100 - self.sales_percent))


class ProductGallery(models.Model):
    """Модель галереи товара"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='product gallery images')

    class Meta:
        verbose_name_plural = 'Галереи товаров'
        verbose_name = 'Галерея товаров'


class ProductRating(models.Model):
    """Модель, чтобы зафиксировать что пользователь поставил оценку для товара"""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)