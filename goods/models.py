from django.core.urlresolvers import reverse
from django.db import models
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
    image = models.ImageField()
    creator = models.ForeignKey(WebStoreUser)
    quantity_in_stock = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('goods_detail', kwargs={'pk': self.pk})


class Order(models.Model):
    products = models.ManyToManyField(Product)
    customer = models.ForeignKey(WebStoreUser)
    total_price = models.FloatField(null=True)
    date = models.DateField(null=True)
    state = models.CharField(max_length=10, default='New')

    def __str__(self):
        return 'Order №' + str(self.pk)
