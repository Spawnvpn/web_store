from django.core.urlresolvers import reverse
from django.db import models
from users.models import WebStoreUser


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})


class Product(models.Model):
    name = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category)
    specifications = models.CharField(max_length=500)
    description = models.TextField(max_length=2000)
    cost = models.FloatField()
    image = models.ImageField()
    creator = models.ForeignKey(WebStoreUser)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('goods_detail', kwargs={'pk': self.pk})
