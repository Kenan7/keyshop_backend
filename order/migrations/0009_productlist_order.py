# Generated by Django 3.1.3 on 2021-01-14 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20210114_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='order.order'),
        ),
    ]
