from django.core.urlresolvers import reverse
from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail
from users.models import WebStoreUser


class Category(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey("self", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})


class Product(models.Model):
    name = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category)
    specifications = models.CharField(max_length=500)
    description = models.TextField(max_length=2000)
    price = models.FloatField()
    image = ImageField()
    creator = models.ForeignKey(WebStoreUser)
    quantity_in_stock = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.image:
            self.image = get_thumbnail(self.image, '600x600', quality=99,
                                       format='JPEG').url
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('goods_detail', kwargs={'pk': self.pk})


class Order(models.Model):
    NEW = 0
    PROCESS = 1
    DONE = 2

    STATE_CHOICES = (
        (NEW, "New"),
        (PROCESS, "In process"),
        (DONE, "Done"),
    )

    customer = models.ForeignKey(WebStoreUser)
    total_price = models.FloatField(null=True)
    date = models.DateField(null=True)
    state = models.IntegerField(choices=STATE_CHOICES, default=NEW)
    city = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return 'Order №' + str(self.pk)


class SubOrder(models.Model):
    order = models.ForeignKey(Order, related_name="suborders")
    product = models.ForeignKey(Product, related_name="suborders_for_product")
    count = models.PositiveIntegerField()

    def __str__(self):
        return "Sub order for " + str(self.order)


from goods import signals