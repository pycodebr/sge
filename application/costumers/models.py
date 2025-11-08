from django.db import models


class Costumer(models.Model):
    name = models.CharField(max_length=50)
    mail = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    document_id = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    active = models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
