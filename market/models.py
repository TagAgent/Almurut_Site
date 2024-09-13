from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models




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
        null=True,
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


class ProductGallery(models.Model):
    """Модель галереи товара"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='product gallery images')

    class Meta:
        verbose_name_plural = 'Галереи товаров'
        verbose_name = 'Галерея товаров'


class ProductRating(models.Model):
    """Модель, чтобы зафиксировать что пользователь поставил оценку для товара"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5)],
        verbose_name='оценка'
    )
    comment = models.TextField(null=True, blank=True, verbose_name='комментарий')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.rating}'

    class Meta:
        verbose_name_plural = 'Оценки товаров'
        verbose_name = 'Оценка товара'
        unique_together = ('product', 'user')
