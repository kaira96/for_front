from django.contrib import admin
from mainapp.models import (
    Semifinished,
    Catalog, Elaboration,
    Brand, Country
)


admin.site.register(Semifinished)
admin.site.register(Catalog)
admin.site.register(Elaboration)
admin.site.register(Brand)
admin.site.register(Country)
