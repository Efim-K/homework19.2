# Generated by Django 5.1 on 2024-09-21 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="token",
            field=models.CharField(
                blank="True", max_length=100, null="True", verbose_name="Token"
            ),
            preserve_default="True",
        ),
    ]
