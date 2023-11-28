# Generated by Django 4.2.6 on 2023-11-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0023_privacypolicy'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
                ('shipping_content', models.TextField(max_length=5000, null=True)),
            ],
        ),
    ]
