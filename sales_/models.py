from django.db import models

from staff.models import Worker
from mainapp.models import Catalog


class SaleWorker(models.Model):
    worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        verbose_name="Сотрудник"
    )
    catalog = models.ManyToManyField(
        Catalog,
        verbose_name="Каталог"
    )
    pairs_shoes = models.PositiveSmallIntegerField(
        verbose_name='Пара обуви'
    )
    price = models.PositiveSmallIntegerField(
        verbose_name='Цена'
    )

    @property
    def sum_of_price(self):
        return self.pairs_shoes * self.price

    def __str__(self):
        return f'{self.worker.full_name} - {self.pairs_shoes} пар обуви - {self.price} сом'

    class Meta:
        verbose_name = 'Журнал продаж'
        verbose_name_plural = 'Журналы продаж'
