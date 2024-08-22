import json
from pathlib import Path
from django.core.management import BaseCommand

from catalog.models import Product, Category

catalog_json = Path(__file__).parent.parent.parent.parent.joinpath("catalog.json")


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        # Здесь мы получаем данные из фикстур с категориями
        with open(catalog_json, 'r', encoding='utf-8') as file:
            categories = json.load(file)
        return categories

    @staticmethod
    def json_read_products():
        # Открываем файл с фикстурами продуктов
        with open(catalog_json, 'r', encoding='utf-8') as file:
            products = json.load(file)
        return products

    def handle(self, *args, **options):
        # Удаляем все продукты из базы данных
        Product.objects.all().delete()
        # Удаляем все категории из базы данных
        Category.objects.all().delete()

        # Создаем списки для хранения объектов категорий и продуктов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фикстуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            if category['model'] == 'catalog.category':
                category_for_create.append(
                    Category(
                        name=category['fields']['name'],
                        depiction=category['fields']['depiction'],
                        pk=category['pk'],
                    )
                )

        # Создаем объекты категорий в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фикстуры для получения информации
        # об одном объекте
        for product in Command.json_read_products():
            if product['model'] == 'catalog.product':
                product_for_create.append(
                    Product(
                        name=product['fields']['name'],
                        depiction=product['fields']['depiction'],
                        price_buy=product['fields']['price_buy'],
                        preview=product['fields']['preview'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'],
                    )
                )

        # Создаем объекты продуктов в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
