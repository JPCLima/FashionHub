# Generated by Django 4.2.3 on 2023-07-31 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_shippingaddress'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': 'Customer'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name_plural': 'OrderItem'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name_plural': 'ShippingAddress'},
        ),
    ]