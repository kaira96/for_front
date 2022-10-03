from django.db import models

from staff.models import Worker, TabelWorkers


# class PUCalculation:
#     class Meta


class TotalSalary(models.Model):
    POSITIONS = (
        ('CLEANER', 'Техничка'),
        ('COOK', 'Повар'),
        ('SEW', 'Швея'),
        ('PU_WORKER', 'Работник ПУ'),
        ('EVA_WORKER', 'Работник ЭВА'),
        ('HANDMAKER', 'Работник'),

    )
    tabel_employer = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE,
        verbose_name='ФИО'
    )
    job_title = models.CharField(
        max_length=255,
        choices=POSITIONS,
        verbose_name='Должность'

    )
    working_day = models.PositiveSmallIntegerField(
        verbose_name='Рабочие дни'
    )
    actual_day = models.PositiveSmallIntegerField(
        verbose_name='Фактически отработанные дни'
    )
    social_salary = models.PositiveSmallIntegerField(
        verbose_name='Оклад СФ'
    )
    debt = models.PositiveSmallIntegerField(
        verbose_name='Задолжность'
    )
    actual_salary = models.PositiveSmallIntegerField(
        verbose_name='Фактически оклад'
    )
    social_fund = models.PositiveSmallIntegerField(
        verbose_name='Соц.Фонд'
    )
    employer_social_fund = models.PositiveSmallIntegerField(
        verbose_name='Работодатель СФ'
    )
    accrued_salary = models.PositiveSmallIntegerField(
        verbose_name='Оклад по начислениям'
    )
    piecework_PU = models.PositiveSmallIntegerField(
        verbose_name='Сдельная станок ПУ'
    )
    piecework_EVA = models.PositiveSmallIntegerField(
        verbose_name='Сдельная ЕВА'
    )
    accrued = models.PositiveSmallIntegerField(
        verbose_name='Начислено'
    )
    premium = models.PositiveSmallIntegerField(
        verbose_name='Премия'
    )
    avans = models.PositiveSmallIntegerField(
        verbose_name='Аванс'
    )
    sale_goods = models.PositiveSmallIntegerField(
        verbose_name='Продажа товаров'
    )
    pay = models.PositiveSmallIntegerField(
        verbose_name='Выплата'
    )
    rest = models.PositiveSmallIntegerField(
        verbose_name='Остаток'
    )
    date = models.DateField(
        verbose_name='Дата'
    )

    # @property
    # def pay(self):
    #     return (
    #
    #     )

    def __str__(self):
        return f'Зарплата {self.tabel_employer.full_name} на {self.date} число'

    class Meta:
        verbose_name = 'Общая зарплата'
        verbose_name_plural = 'Общие зарплаты'
