# Generated by Django 5.1 on 2024-08-21 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("name",),
                "verbose_name": "Наименование",
                "verbose_name_plural": "Наименования",
            },
        ),
    ]
