from django.contrib import admin

from stocks.models import StockOfDoneProducts


# Register your models here.
@admin.register(StockOfDoneProducts)
class StockOfDoneProductsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'quantity', 'date']
    list_display_links = ['__str__']
