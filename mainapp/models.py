from django.db import models


class Country(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название страны'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Brand(models.Model):
    title = models.CharField(max_length=255, verbose_name='Бренд обуви')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бренд обуви'
        verbose_name_plural = 'Бренды обуви'


class Semifinished(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    country = models.ForeignKey(
        Country, 
        on_delete=models.CASCADE,
        verbose_name='Страна'
    )

    @property
    def total_rest(self):
        stock = Semifinished.objects.all()
        stock_quantity = Semifinished.objects.count()
        return sum(
            [stock[i].quantity for i in range(stock_quantity)]
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Полуфабрикат'
        verbose_name_plural = 'Полуфабрикаты'


class Catalog(models.Model):
    model = models.CharField(
        verbose_name='Код товара',
        max_length=20
    )
    color = models.CharField(
        max_length=50,
        verbose_name='Цвет'
    )
    picture = models.ImageField(
        upload_to='images/catalog',
        verbose_name='Изображение',
        null=True, blank=True
    )
    size_from = models.PositiveSmallIntegerField(
        verbose_name='Размер от'
    )
    size_to = models.PositiveSmallIntegerField(
        verbose_name='Размер до'
    )
    articul = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name='Артикул(Бренд товара)'
    )

    def __str__(self):
        return f'{self.articul.title} - {self.color} - {self.model}'

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'


class Elaboration(models.Model):
    semifinished = models.ForeignKey(
        Semifinished,
        on_delete=models.CASCADE,
        verbose_name='полуфабрикаты'
    )
    quantity_of_pairs = models.PositiveSmallIntegerField(
        verbose_name='Сколько произведено'
    )
    quantity_of_packages = models.PositiveSmallIntegerField(
        verbose_name='Сколько упаковок'
    )
    catalog = models.ManyToManyField(
        Catalog,
        verbose_name='Каталог'
    )
    defect_working = models.PositiveSmallIntegerField(
        verbose_name='рабочий брак'
    )
    quantity_of_PU = models.PositiveSmallIntegerField(
        verbose_name='Количество пар ПУ'
    )
    quantity_of_EVA = models.PositiveSmallIntegerField(
        verbose_name='Количество пар ЭВА'
    )
    defect_EVA = models.PositiveSmallIntegerField(verbose_name='Брак ЭВА')
    defect_PU = models.PositiveSmallIntegerField(verbose_name='Брак ПУ')
    date = models.DateField(verbose_name='Дата')
    to_stock = models.PositiveSmallIntegerField(
        verbose_name='Сколько отправят на склад'
    )
    total_defect = models.PositiveSmallIntegerField(
        verbose_name='Общее количество брака'
    )
    total_price = models.PositiveSmallIntegerField(
        verbose_name='Общая цена'
    )

    @property
    def quantity_of_pairs_with_defect_calculation(self):
        return self.quantity_of_pairs - self.total_defect

    def __str__(self):
        return f'Выработано {self.quantity_of_pairs}'

    class Meta:
        verbose_name = 'Выработка'
        verbose_name_plural = 'Выработки'
