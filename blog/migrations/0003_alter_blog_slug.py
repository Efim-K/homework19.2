# Generated by Django 5.1 on 2024-09-01 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_blog_preview"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.CharField(
                blank="True", max_length=200, null="True", verbose_name="slug"
            ),
        ),
    ]
