from django.db import models
from django.core.validators import RegexValidator


class Worker(models.Model):
    POSITIONS = (
        ('Техничка', 'Техничка'),
        ('Повар', 'Повар'),
        ('Швея', 'Швея'),
        ('Работник ПУ', 'Работник ПУ'),
        ('Работник ЭВА', 'Работник ЭВА'),
        ('Работник', 'Работник'),
        ('Работник Склада', 'Работник Склада'),
        ('Бухгалтер', 'Бухгалтер')
    )
    full_name = models.CharField(
        max_length=200,
        verbose_name="Ф.И.О."
    )
    image = models.ImageField(
        upload_to='images/Worker/%Y',
        verbose_name='Фото',
        null=True, blank=True
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
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='Почта',
        null=True, blank=True
    )
    job_title = models.CharField(
        max_length=255,
        choices=POSITIONS,
        verbose_name='Должность'
    )
    date_joined = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата регистрации'
    )

    def __str__(self):
        return f'{self.full_name} - {self.job_title}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class TabelWorkers(models.Model):
    worker = models.ManyToManyField(
        Worker,
        verbose_name='Сотрудник',
    )
    date = models.DateField(
        null=True,
        verbose_name='Дата'
    )
    quantity_of_PU = models.PositiveSmallIntegerField(
        verbose_name='Количество пар ПУ'
    )
    quantity_of_EVA = models.PositiveSmallIntegerField(
        verbose_name='Количество пар ЭВА'
    )
    total_quantity = models.PositiveSmallIntegerField(
        verbose_name='Общее количество'
    )
    total_defect = models.PositiveSmallIntegerField(
        verbose_name='Общее браки',
        default=0
    )
    price_of_single_mmodel = models.PositiveSmallIntegerField(
        verbose_name='цена'
    )
    total_price_of_one_worker = models.PositiveSmallIntegerField(
        verbose_name='Полная цена'
    )  # Цена продуктов

    @property
    def total_defect_of_all_workers(self):  # Общая сумма браков сделанных всеми сотрудниками
        workers = TabelWorkers.objects.filter(
            date=self.date
        )
        return sum([i.total_defect for i in workers])

    # @property
    # def total_price_of_single_worker(self):  #Оклад за выработанные продукты без учета браков одного сотрудника
    #     workers = TabelWorkers.objects.filter(
    #         date=self.date
    #     )
    #     return round(
    #         sum(
    #             [i.total_price_of_one_worker for i in workers]
    #         ) / workers.count()
    #     )

    @property
    def total_price(self):  # Общая зп всех сотрудников без учета браков
        workers = TabelWorkers.objects.filter(
            date=self.date
        )
        return round(
            sum(
                [i.total_price_of_one_worker for i in workers]
            )
        )

    @property
    def final_salary_with_defect_calculation(self):  # Финальная зп за день
        workers = TabelWorkers.objects.filter(
            date=self.date
        ).count()
        return round(
            self.total_price - (
                    (self.total_defect_of_all_workers * 200) / workers
            )
        )

    # @property
    # def final_salary_of_single_worker_per_day(self):
    #     return self.total_price_of_single_worker - \
    #         self.defect_of_single_worker_per_day

    def __str__(self):
        return f'Табель на {self.date}'

    class Meta:
        verbose_name = 'Табель сотрудника'
        verbose_name_plural = 'Табель сотрудников'
