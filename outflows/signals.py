# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Outflow


@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, **kwargs):
    if instance.quantity > 0:
        product = instance.product
        product.quantity -= instance.quantity
        product.save()
