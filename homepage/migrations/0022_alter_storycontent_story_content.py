# Generated by Django 4.2.6 on 2023-11-28 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0021_storycontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storycontent',
            name='story_content',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]
