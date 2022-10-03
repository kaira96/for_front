from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed

from calendar_1.models import ModelCalendarPU, ModelCalendarEVA

from daily_diary.models import DailyDiary

from mainapp.models import (
    Elaboration, Semifinished
)

from staff.models import TabelWorkers

from stocks.models import StockOfDoneProducts


@receiver(post_save, sender=DailyDiary)
def automatic_stock_of_done_products(
        sender, instance, created, **kwargs
    ):
    if created:
        try:
            s = Semifinished.objects.get(pk=instance.semifinished.pk)
            s.quantity -= instance.quantity_of_pairs
            s.save()
        except:
            raise AttributeError(
                'У вас недостаточно полуфабрикатов. Пополните запасы.'
            )
        print('Object semifinished updated!')


@receiver(
    m2m_changed, 
    sender=DailyDiary.catalog.through and DailyDiary.worker.through
)
def automatic_catalog(sender, instance, action, **kwargs):
    if action == 'pre_add':
        elaboration = Elaboration.objects.create(
            semifinished=instance.semifinished,
            quantity_of_packages=instance.package,
            defect_working=instance.SAYA_defect,
            defect_EVA=instance.EVA_defect,
            defect_PU=instance.PU_defect,
            to_stock=instance.to_stock,
            quantity_of_PU=instance.quantity_of_PU,
            quantity_of_EVA=instance.quantity_of_EVA,
            quantity_of_pairs=instance.quantity_of_pairs,
            total_defect=instance.total_defect,
            total_price=instance.total_price,
            date=instance.date
        )
        stock = StockOfDoneProducts.objects.create(
            quantity=instance.to_stock,
            date=instance.date
        )
        model_calendar_pu = ModelCalendarPU.objects.create(
            quantity_of_PU=instance.total_PU,
            date=instance.date
        )
        model_calendar_eva = ModelCalendarEVA.objects.create(
            quantity_of_EVA=instance.total_EVA,
            date=instance.date
        )
        for i in instance.catalog.all():
            elaboration.catalog.add(i)
            stock.catalog.add(i)
            model_calendar_pu.catalog.add(i)
            model_calendar_eva.catalog.add(i)
        elaboration.save()
        stock.save()
        print('Elaboration created!')
        print('Stock created!')
        print('ModelCalendarPU created')
    elif action == 'post_add':
        tabel = TabelWorkers.objects.create(
            date=instance.date,
            total_quantity=instance.quantity_of_pairs,
            total_defect=instance.total_defect,
            total_price_of_one_worker=instance.total_price,
            quantity_of_EVA=instance.quantity_of_EVA,
            quantity_of_PU=instance.quantity_of_PU,
            price_of_single_mmodel=instance.price,
        )
        for i in instance.worker.all():
            tabel.worker.add(i)
        tabel.save()
        print('Tabel of workers has been created!')
