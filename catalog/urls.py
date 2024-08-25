from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import product_list, product_detail, contacts

app_name = CatalogConfig.name
urlpatterns = [
    path("", product_list, name="product_list"),
    path("product/<int:pk>/", product_detail, name="product_detail"),
    path("contacts/", contacts, name="contacts"),
]
