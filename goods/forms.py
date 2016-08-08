from django import forms
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


class CheckOutForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'city',
            'address',
        )

# class OrderForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#     state = forms.CharField(widget=Select(
#         choices=(('New', 'New'), ('Process', 'Process'), ('Done', 'Done'),)),)
#
#     class Meta:
#         model = Order
#         fields = '__all__'
