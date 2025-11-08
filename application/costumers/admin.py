from django.contrib import admin
from . import models


class CostumerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'phone', 'document_id', 'social_media','address', 'city' , 'state' , 'zip_code')
    search_fields = ('name',)


admin.site.register(models.Costumer, CostumerAdmin)
