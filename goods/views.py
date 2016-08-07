import time

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from goods.forms import ProductCreateForm
from goods.models import Product, Order
from django.http import HttpResponse
from carton.cart import Cart


class GoodsListView(ListView):
    model = Product
    context_object_name = 'product_list'


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
    model = Product
    form_class = ProductCreateForm


class GoodsDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


def add(request):
    cart = Cart(request.session)
    product = Product.objects.get(pk=request.GET.get('product_id'))
    cart.add(product, price=product.price)
    return HttpResponse("Added")


def show(request):
    return render(request, 'goods/show_cart.html')


def remove(request):
    cart = Cart(request.session)
    product = Product.objects.get(id=request.GET.get('id'))
    cart.remove(product)
    if request.is_ajax():
        return HttpResponse("Item removed")


def checkout(request):
    if request.method == 'POST':
        cart = Cart(request.session)
        order = Order()
        order.date = timezone.now()
        order.customer = request.user
        order.total_price = cart.total
        order.save()
        for pk in request.session.get('CART'):
            order.products.add(Product.objects.get(pk=request.session.get('CART').get(pk).get('product_pk')))
        order.save()
        cart.clear()
        return HttpResponse("Done")
    return render(request, 'goods/checkout.html')
