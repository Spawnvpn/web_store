from django import forms
from goods.models import Product


class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'name',
            'categories',
            'specifications',
            'description',
            'cost',
            'image',
        )