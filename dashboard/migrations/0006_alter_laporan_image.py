# Generated by Django 3.2.2 on 2021-05-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_barang_jenis_barang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laporan',
            name='image',
            field=models.ImageField(default='/item/default.jpg', upload_to='item'),
        ),
    ]
