from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from goods.forms import ProductCreateForm
from goods.models import Product, Order, SubOrder
from django.http import HttpResponse
from carton.cart import Cart
from django.utils.translation import ugettext as _


class GoodsListView(ListView):
    model = Product
    context_object_name = 'product_list'

    def get_queryset(self):
        qs = super(GoodsListView, self).get_queryset()
        q = self.request.GET.get('q')
        if q is not None:
            sort_by = self.request.GET.get('by')
            if sort_by is not None:
                sort_by = self.request.GET.get('in') + sort_by.lower()
            else:
                sort_by = 'price'
            return Product.objects.filter(Q(name__icontains=q) |
                                          Q(specifications__icontains=q) |
                                          Q(price__icontains=q) |
                                          Q(quantity_in_stock__icontains=q)).order_by(sort_by)
        return qs


class GoodsDetailView(DetailView):
    model = Product
    context_object_name = 'product'


class GoodsCreateView(CreateView):
    form_class = ProductCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class GoodsUpdateView(UpdateView):
    template_name = 'goods/product_update.html'
    model = Product
    form_class = ProductCreateForm


class GoodsDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


def add(request):
    cart = Cart(request.session)
    product = Product.objects.get(pk=request.GET.get('product_id'))
    cart.add(product, price=product.price)
    return HttpResponse(_("Added"))


def show(request):
    return render(request, 'goods/show_cart.html')


def remove(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('id'))
    cart.remove(product)
    if request.is_ajax():
        return HttpResponse(_("Item removed"))


def checkout(request):
    if request.method == 'POST':
        cart = Cart(request.session)
        order = Order(
            date=timezone.now(),
            customer=request.user,
            total_price=cart.total,
            city=request.POST.get('city'),
            address=request.POST.get('address'),
        )
        order.save()
        for item in cart.items:
            sub_order = SubOrder(
                product=item.product,
                quantity=item.quantity,
                order=order,
            )
            sub_order.save()
        cart.clear()
        return HttpResponse(request)
    return render(request, 'goods/checkout.html')
