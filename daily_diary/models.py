from django.db import models

from mainapp.models import Semifinished, Catalog

from staff.models import Worker, TabelWorkers


class DailyDiary(models.Model):
    catalog = models.ManyToManyField(
        Catalog,
        verbose_name='Каталог'
    )
    price = models.PositiveSmallIntegerField(
        verbose_name='Цена'
    )
    worker = models.ManyToManyField(
        Worker,
        verbose_name='Сотрудник'
    )
    package_pairs = models.PositiveSmallIntegerField(
        default=6,
        verbose_name='Сколько пар в одной упаковке'
    )
    quantity_of_PU = models.PositiveSmallIntegerField(
        verbose_name='Количество пар ПУ'
    )
    quantity_of_EVA = models.PositiveSmallIntegerField(
        verbose_name='Количество пар ЭВА'
    )
    semifinished = models.ForeignKey(
        Semifinished,
        on_delete=models.CASCADE,
        verbose_name='Полуфабрикаты'
    )
    worker_defect = models.PositiveSmallIntegerField(
        verbose_name='Количество рабочего брака'
    )
    SAYA_defect = models.PositiveSmallIntegerField(
        verbose_name='Количество брака САЯ'
    )
    PU_defect = models.PositiveSmallIntegerField(
        verbose_name='Количество брака ПУ'
    )
    EVA_defect = models.PositiveSmallIntegerField(
        verbose_name='Количество брака ЭВА'
    )
    date = models.DateField(null=True, verbose_name='Дата')

    def __str__(self):
        return f'Ежедневка на {self.date}'

    @property
    def quantity_of_pairs(self):
        return sum(
            (
                self.quantity_of_PU,
                self.quantity_of_EVA
            )
        )

    @property
    def package(self):
        return (
            self.quantity_of_pairs // self.package_pairs
        )

    @property
    def package_rest(self):
        return (
            self.quantity_of_pairs % self.package_pairs
        )

    @property
    def total_price(self):
        return self.price * self.quantity_of_pairs

    @property
    def total_PU(self):
        return self.quantity_of_PU - self.PU_defect

    @property
    def total_EVA(self):
        return self.quantity_of_EVA - self.EVA_defect

    @property
    def total_defect(self):  # Общее количество браков
        return sum(
            (
                self.SAYA_defect,
                self.PU_defect,
                self.EVA_defect,
                self.worker_defect
            )
        )

    @property
    def to_stock(self):
        return self.quantity_of_pairs - self.total_defect

    class Meta:
        verbose_name = 'Ежедневка'
        verbose_name_plural = 'Ежедневки'
