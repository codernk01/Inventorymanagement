# Generated by Django 4.1 on 2022-08-12 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0004_inventory_factory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='factory',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app_control.factory'),
        ),
    ]
