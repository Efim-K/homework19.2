from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, contacts, ProductCreateView, ProductDeleteView, \
    ProductUpdateView, CategoryListView

app_name = CatalogConfig.name
urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("contacts/", contacts, name="contacts"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
]
