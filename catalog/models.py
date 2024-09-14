from django.db import models

# Create your models here.
NULLABLE = {"blank": "True", "null": "True"}


class Product(models.Model):
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
