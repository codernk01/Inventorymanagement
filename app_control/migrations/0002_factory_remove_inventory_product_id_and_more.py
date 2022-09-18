# Generated by Django 4.1 on 2022-08-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factory_name', models.CharField(max_length=50)),
                ('factory_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='product_id',
        ),
        migrations.AddField(
            model_name='inventory',
            name='product_description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]