from django.contrib import admin
from . import models


class OutflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'created_at', 'updated_at',)
    search_fields = ('supplier__name', 'product__title',)


admin.site.register(models.Outflow, OutflowAdmin)
