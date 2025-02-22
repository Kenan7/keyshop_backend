# Generated by Django 3.1.3 on 2020-11-25 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_product_image_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="stock_amount",
            new_name="quantity",
        ),
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.CharField(default="text", max_length=1000),
            preserve_default=False,
        ),
    ]
