# Generated by Django 4.2.6 on 2023-11-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_remove_kurti_l42_remove_kurti_m40_remove_kurti_s38_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kurti',
            name='available_sizes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
