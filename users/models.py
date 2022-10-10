from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    is_stockman = models.BooleanField(
        default=False,
        verbose_name = 'Является ли начальником склада'
    )
    is_accountant = models.BooleanField(
        default=False,
        verbose_name = 'Является ли бухгалтером'
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,20}$',
        message='+996111222333'
    )
    phone = models.CharField(
        validators=[phone_regex],
        max_length=30,
        unique=True,
        verbose_name='Номер телефона'
    )

    @property
    def full_name(self):
        return self.get_full_name()

    @property
    def job_title(self):
        return 'Работник Склада' if self.is_stockman else 'Бухгалтер'
