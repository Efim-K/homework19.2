from django.contrib import admin
from catalog.models import Product
from catalog.models import Category


# Register your models here.
@admin.register(Product)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_buy', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'depiction',)


@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
