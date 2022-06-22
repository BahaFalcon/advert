from django.db import models

from users.models import User


class ProductCategory(models.Model):
    """Модель для категорий"""
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    """Мoдель для товаров"""
    author = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE,
                                 null=True, verbose_name='Категория', related_name='products')
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    @property
    def category_name(self):
        return self.category.title

    def __str__(self):
        return self.name





