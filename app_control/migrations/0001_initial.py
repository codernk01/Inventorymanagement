# Generated by Django 4.1 on 2022-08-09 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(max_length=10, unique=True)),
                ('product_name', models.CharField(max_length=50)),
                ('product_quantity', models.PositiveIntegerField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
