# Generated by Django 4.1 on 2022-08-16 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0006_remove_inventory_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='factory',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app_control.factory'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
