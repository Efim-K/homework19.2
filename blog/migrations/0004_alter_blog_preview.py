# Generated by Django 5.1 on 2024-09-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_blog_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="preview",
            field=models.ImageField(
                blank="True", null="True", upload_to="blog/", verbose_name="Превью"
            ),
        ),
    ]
