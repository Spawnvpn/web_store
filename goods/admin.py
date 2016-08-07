from goods.forms import OrderForm
from goods.models import Product, Category, Order
from django.contrib import admin


class PriceFilter(admin.SimpleListFilter):
    title = 'Sum category'
    parameter_name = 'total_price'

    def queryset(self, request, queryset):
        if request.user.is_superuser:
            return super(PriceFilter,
                         self).queryset(request, queryset)

    def lookups(self, request, model_admin):
        """
        Only show the lookups if there actually is
        anyone born in the corresponding decades.
        """
        qs = model_admin.get_queryset(request)
        if qs.filter(total_price__gte=1,
                     total_price__lte=100).exists():
            yield ('from 1 to 100 dollars', ('in the eighties'))
        if qs.filter(total_price__gte=100,
                     total_price__lte=1000).exists():
            yield ('from 100 to 1000 dollars', ('in the nineties'))


class CategoriesInline(admin.TabularInline):
    model = Product.categories.through


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
    # list_display = ['categories', 'price']
    # list_editable = ('categories', 'price')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    list_filter = (
        'total_price',
    )

