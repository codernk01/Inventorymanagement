# Generated by Django 4.1 on 2022-08-16 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0005_alter_inventory_factory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='product_Img',
        ),
    ]
