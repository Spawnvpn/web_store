from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from goods.forms import ProductCreateForm
from goods.models import Product


class GoodsListView(ListView):
    model = Product
    context_object_name = 'goods_list'


class GoodsDetailView(DetailView):
    model = Product


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