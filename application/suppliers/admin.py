from django.contrib import admin
from . import models


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'phone', 'site', 'document_id', 'contact', 'contact_phone', 'address', 'city' , 'state' , 'zip_code', 'description')
    search_fields = ('name',)


admin.site.register(models.Supplier, SupplierAdmin)
