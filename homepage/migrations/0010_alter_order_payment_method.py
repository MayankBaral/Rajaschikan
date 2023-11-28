# Generated by Django 4.2.6 on 2023-11-13 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_remove_order_productitem_alter_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'), ('upi', 'UPI'), ('cash_on_delivery', 'Cash on Delivery')], max_length=20),
        ),
    ]
