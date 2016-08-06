from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from goods.forms import ProductCreateForm
from goods.models import Product
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
    product = Product.objects.get(id=request.GET.get('product_id'))
    cart.add(product, price=product.cost)
    return HttpResponse("Added")


def show(request):
    return render(request, 'goods/show_cart.html')
