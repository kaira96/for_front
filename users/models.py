from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_stock_man = models.BooleanField(
        default=False,
        verbose_name = 'Является ли начальником склада'
    )
    is_accountant = models.BooleanField(
        default=False,
        verbose_name = 'Является ли бухгалтером'
    )
