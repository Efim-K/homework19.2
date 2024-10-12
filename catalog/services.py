from catalog.models import Product
from config.settings import CAСHE_ENABLED
from django.core.cache import cache


def get_product_from_cache():
    """
    Получает продукт из кэша, если кэш пустой, получаем данные из БД
    """
    if not CAСHE_ENABLED:
        return Product.objects.all()

    cache_key = "product_list"
    products = cache.get(cache_key)

    # Если кэш не пустой, возвращаем данные из кэша
    if products is not None:
        return products

    # Если кэш пустой, получаем данные из БД и добавляем их в кэш
    products = Product.objects.all()
    cache.set(cache_key, products)  # Cache for 1 hour
    return products
