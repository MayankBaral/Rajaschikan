# Generated by Django 4.2.6 on 2023-11-17 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0017_alter_orderitems_size_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='keywords',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
