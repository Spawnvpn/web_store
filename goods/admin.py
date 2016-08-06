from goods.models import Product, Category
from django.contrib import admin


class CategoriesInline(admin.TabularInline):
    model = Product.categories.through


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['categories', 'cost']
    list_editable = ('categories', 'cost')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
