from django.shortcuts import render, get_object_or_404

from catalog.forms import ProductForm
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name}\n{phone}\n{message}")
    return render(request, "contacts.html")
