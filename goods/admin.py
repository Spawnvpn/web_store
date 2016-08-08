from goods.models import Product, Category, Order, SubOrder
from django.contrib import admin


class PriceFilter(admin.SimpleListFilter):
    title = 'Sum category'
    parameter_name = 'total_price'

    def queryset(self, request, queryset):
        if self.value() == '1..100':
            return queryset.filter(total_price__gte=1,
                                   total_price__lte=100)
        if self.value() == '100..1000':
            return queryset.filter(total_price__gte=100,
                                   total_price__lte=1000)
        if self.value() == '1000..10000':
            return queryset.filter(total_price__gte=1000,
                                   total_price__lte=10000)

    def lookups(self, request, model_admin):

        qs = model_admin.get_queryset(request)
        if qs.filter(total_price__gte=1,
                     total_price__lte=100).exists():
            yield ('1..100', '1..100')
        if qs.filter(total_price__gte=100,
                     total_price__lte=1000).exists():
            yield ('100..1000', '100..1000')
        if qs.filter(total_price__gte=1000,
                     total_price__lte=10000).exists():
            yield ('1000..10000', '1000..10000')


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


class SubOrderInline(admin.TabularInline):
    model = SubOrder


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # form = OrderForm
    list_display = ('order_id', 'customer', 'state', 'total_price')
    list_editable = ('state', 'total_price')
    list_filter = (
        PriceFilter,
    )
    inlines = (
        SubOrderInline,
    )

    def order_id(self, obj):
        return str(obj)
    order_id.short_description = "Order ID"


@admin.register(SubOrder)
class SubOrder(admin.ModelAdmin):
    pass
