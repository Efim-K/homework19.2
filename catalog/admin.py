from django.contrib import admin
from catalog.models import Product, Version, Category


# Register your models here.
@admin.register(Product)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price_buy", "category")
    list_filter = ("category",)
    search_fields = (
        "name",
        "depiction",
    )


@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "version_number",
        "version_name",
        "version_active",
    )
