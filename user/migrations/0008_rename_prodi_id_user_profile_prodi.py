# Generated by Django 3.2.2 on 2021-05-09 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210509_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='prodi_id',
            new_name='prodi',
        ),
    ]