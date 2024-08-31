from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name}\n{phone}\n{message}")
    return render(request, "contacts.html")
