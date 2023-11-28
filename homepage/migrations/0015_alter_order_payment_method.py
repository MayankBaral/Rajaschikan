# Generated by Django 4.2.6 on 2023-11-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_product_in_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('cash_on_delivery', 'Cash on Delivery'), ('pay_online', 'Pay Online')], max_length=20),
        ),
    ]
