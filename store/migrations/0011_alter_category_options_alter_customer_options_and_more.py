# Generated by Django 4.2.3 on 2023-07-31 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_category_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'OrderItem'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product'},
        ),
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name': 'ShippingAddress'},
        ),
    ]
