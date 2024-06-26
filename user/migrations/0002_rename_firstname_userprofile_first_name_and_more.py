# Generated by Django 4.2.6 on 2023-10-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='e_mail',
            field=models.EmailField(default=' ', max_length=254),
        ),
    ]
