from django.dispatch import receiver
from django.db.models.signals import m2m_changed

from calendar_1.models import ElaborationCalendar
from mainapp.models import Elaboration


@receiver(
    m2m_changed, 
    sender=Elaboration.catalog.through
)
def automatic_catalog_calendar_elaboration(
    sender, 
    instance, 
    action,
    **kwargs
):
    print(f'\n\n\n\n\n\n\n ACTION IS {action} \n\n\n\n\n\n\n')

    if action == 'post_add':
        print(f'\n\n\n\n\n\n\n ACTION IN FUNC IS {action} \n\n\n\n\n\n\n')
        elaboration_calendar = ElaborationCalendar.objects.create(
            elaboration=instance,
            date=instance.date,
        )
        for i in instance.catalog.all():
            elaboration_calendar.catalog.add(i)
            elaboration_calendar.save()
        print('Elaboration calendar has been created!')
