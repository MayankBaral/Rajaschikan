# Generated by Django 4.2.6 on 2023-11-11 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabric',
            name='available_sizes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='saree',
            name='available_sizes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
