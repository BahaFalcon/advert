from django.db import models


class User(models.Model):
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=5, unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
