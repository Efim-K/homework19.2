from django.shortcuts import render, get_object_or_404
from catalog.models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "products_list.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, "product_detail.html", context)


# def home(request):
#     return render(request, "home.html")
#
#
# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         print(f"{name} \n{phone} \n{message}\n")
#     return render(request, "contacts.html")
