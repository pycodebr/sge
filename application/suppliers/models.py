from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    mail = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    site = models.CharField(max_length=50, blank=True)
    document_id = models.CharField(max_length=15, blank=True)
    contact = models.CharField(max_length=50, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
