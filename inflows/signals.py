# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Inflow


@receiver(post_save, sender=Inflow)
def update_product_quantity(sender, instance, **kwargs):
    if instance.quantity > 0:
        product = instance.product
        product.quantity += instance.quantity
        product.save()
