# Generated by Django 4.2.6 on 2023-11-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0026_cancelrefund'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelrefund',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
