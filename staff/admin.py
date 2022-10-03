from django.contrib import admin
from staff.models import Worker, TabelWorkers


class TabelWorkersAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'date']


# Register your models here.
admin.site.register(Worker)
admin.site.register(TabelWorkers, TabelWorkersAdmin)

# admin.site.register(DoneProduct)


# class TabelWorkerAdmin(admin.TabularInline):
#     model = TabelWorkers
#     extra = 0


# @admin.register(TabelWorkers)
# class TabelAdmin(admin.ModelAdmin):
#     list_display = ['date_today']
#     list_display_links = ['date_today']
#     inlines = [TabelWorkerAdmin]
