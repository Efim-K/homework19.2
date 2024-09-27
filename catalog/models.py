from django.db import models

from users.models import User

# Create your models here.
NULLABLE = {"blank": "True", "null": "True"}


class Product(models.Model):
    """
    Продукт с описанием, изображением, категорией и ценой за покупку.
    """
    name = models.CharField(
        max_length=100, verbose_name="Наименование", help_text="Наименование продукта"
    )
    depiction = models.TextField(
        verbose_name="Описание", help_text="Описание продукта", **NULLABLE
    )
    preview = models.ImageField(
        upload_to="catalog/photo",
        verbose_name="Изображение",
        help_text="Изображение(превью) продукта",
        **NULLABLE,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Категория продукта",
        **NULLABLE,
        related_name="products",
    )
    price_buy = models.IntegerField(
        verbose_name="Цена за покупку",
        help_text="Цена за покупку продукта",
    )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания", help_text="Дата создания(записи в БД) продукта"
                                      )
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name="Дата последнего изменения",
                                      help_text="Дата последнего изменения(записи в БД)продукта",
                                      **NULLABLE,
                                      )
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f"{self.name, self.price_buy}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = (
            "name",
            "category",
            "price_buy",
        )


class Category(models.Model):
    """
    Категория с описанием.
    """
    name = models.CharField(
        max_length=100, verbose_name="Наименование", help_text="Наименование категории"
    )
    depiction = models.TextField(
        verbose_name="Описание", help_text="Описание категории", **NULLABLE
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)


class Version(models.Model):
    """
    Версия продукта с описанием, привязкой к продукту и отметкой активности.
    """
    product = models.ForeignKey(
        "Product",
        related_name="versions",
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        help_text="Продукт, к которому привязана версия",
        **NULLABLE,
    )
    version_number = models.PositiveIntegerField(verbose_name="Номер версии", help_text="Номер версии продукта")
    version_name = models.CharField(max_length=100, verbose_name="Наименование версии",
                                    help_text="Наименование версии продукта")
    version_active = models.BooleanField(default=False, verbose_name="Активная версия",
                                         help_text="Активная версия продукта")

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"
        ordering = (
            'version_name', 'version_number'
        )

    def __str__(self):
        return f"{self.version_name}"
