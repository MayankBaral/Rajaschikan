# Generated by Django 4.2.6 on 2023-11-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0018_product_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tracking_Id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tracking_company',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
