from django.db.models import Count, F
from django.db.models.signals import post_save
from django.dispatch import receiver
from goods.models import Order, Product


@receiver(post_save, sender=Order)
def callback(instance, **kwargs):
    if instance.state == Order.PROCESS:
        (Product.objects
                .filter(suborders_for_product__order=instance)
                .annotate(count=Count("suborders_for_product__count"))
                .update(quantity_in_stock=F("quantity_in_stock")-F("count")))

