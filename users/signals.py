from django.dispatch import receiver
from django.db.models.signals import post_save

from staff.models import Worker

from users.models import User


@receiver(post_save, sender=User)
def auto_creating_worker_after_user(
        sender, instance, created, **kwargs
):
    if created:
        Worker.objects.create(
            full_name=instance.full_name,
            phone=instance.phone,
            email=instance.email,
            job_title=instance.job_title,
            date_joined=instance.date_joined
        )
        print('Worker based on registration created!')
