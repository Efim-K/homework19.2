from catalog.models import Product, Category
from config.settings import CAСHE_ENABLED
from django.core.cache import cache


def get_product_from_cache(catalog_model):
    """
    Получает продукт из кэша, если кэш пустой, получаем данные из БД
    """

    if not CAСHE_ENABLED:
        return catalog_model.objects.all()

    # Получаем имя модели из имени класса
    name_model = catalog_model.__name__.lower()
    # Ключ для кэша, хранящий данные продуктов в модели 'Product' или 'Category' (например, 'product_list')
    cache_key = f"{name_model}_list"
    obj = cache.get(cache_key)

    # Если кэш не пустой, возвращаем данные из кэша
    if obj is not None:
        return obj

    # Если кэш пустой, получаем данные из БД и добавляем их в кэш
    obj = catalog_model.objects.all()
    cache.set(cache_key, obj)
    return obj
