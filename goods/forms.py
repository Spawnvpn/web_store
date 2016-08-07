from django import forms
from django.forms import Select
from goods.models import Product, Order


class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'name',
            'categories',
            'specifications',
            'description',
            "price",
            'image',
        )


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    state = forms.CharField(widget=Select(
        choices=(('New', 'New'), ('Process', 'Process'), ('Done', 'Done'),)),)

    class Meta:
        model = Order
        fields = '__all__'
