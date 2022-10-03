from django.db import models

from mainapp.models import Catalog


class StockBase(models.Model):
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество'
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата'
    )

    def __str__(self):
        return f'{self.quantity} - остаток на складе'

    class Meta:
        abstract = True


class StockOfDoneProducts(StockBase):
    catalog = models.ManyToManyField(
        Catalog,
        verbose_name='Каталог'
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество выработанных продуктов на складе',
        default=0
    )
    date = models.DateField(
        verbose_name='Дата',
        null=True
    )
    @property
    def total_rest(self):
        stock = StockOfDoneProducts.objects.all()
        stock_quantity = StockOfDoneProducts.objects.count()
        return sum(
            [stock[i].quantity for i in range(stock_quantity)]
        )

    class Meta:
        verbose_name = 'Склад готовых продуктов'
        verbose_name_plural = 'Склад готовых продуктов'
