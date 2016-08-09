from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from goods.models import Order, Product, SubOrder


@transaction.non_atomic_requests(using='other')
def decrement_products(qs):
    for so in qs:
        product = so.product
        product.quantity_in_stock -= so.quantity
        product.save()


@receiver(post_save, sender=Order)
def callback(instance, **kwargs):
    if instance.state == Order.PROCESS:
        qs = SubOrder.objects.filter(order=instance).prefetch_related("product")
        decrement_products(qs)

