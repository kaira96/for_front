from django.db import models
from daily_diary.models import DailyDiary
from mainapp.models import Elaboration, Catalog
from staff.models import TabelWorkers


class ElaborationCalendar(models.Model):
    elaboration = models.ForeignKey(  # Вытащим общий брак, количество пар
        Elaboration,
        on_delete=models.CASCADE,
        verbose_name='Общий брак'
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата'
    )
    catalog = models.ManyToManyField(
        Catalog,
        verbose_name='Каталог'
    )

    def __str__(self):
        return str(self.elaboration.date)

    class Meta:
        verbose_name = 'Календарь выработки'
        verbose_name_plural = 'Календари выработки'


class ModelCalendarPU(models.Model):
    quantity_of_PU = models.PositiveSmallIntegerField(
        verbose_name='Количество пар ПУ', null=True
    )
    date = models.DateField(
        null=True,
        verbose_name='Дата'
    )
    catalog = models.ManyToManyField(
        Catalog,
        verbose_name='Каталог'
    )

    def __str__(self):
        return f'{self.date} - {self.quantity_of_PU} пар ПУ'

    class Meta:
        verbose_name = 'Календарь ПУ'
        verbose_name_plural = 'Календари ПУ'


class ModelCalendarEVA(models.Model):
    quantity_of_EVA = models.PositiveSmallIntegerField(
        verbose_name='Количество пар ЭВА', null=True
    )
    date = models.DateField(
        null=True,
        verbose_name='Дата'
    )
    catalog = models.ManyToManyField(
        Catalog,
        verbose_name='Каталог'
    )

    def __str__(self):
        return f'{self.date} - {self.quantity_of_EVA} пар ЭВА'

    class Meta:
        verbose_name = 'Календарь ЭВА'
        verbose_name_plural = 'Календари ЭВА'
