# Generated by Django 3.2.2 on 2021-05-09 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210509_0803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='user',
            new_name='account',
        ),
    ]