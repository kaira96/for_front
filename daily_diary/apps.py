from django.apps import AppConfig


class DailyDiaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'daily_diary'
    verbose_name = 'Ежедневник'

    def ready(self):
        import daily_diary.signals
