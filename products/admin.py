from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'serie_number',)
    search_fields = ('title',)


admin.site.register(models.Product, ProductAdmin)
