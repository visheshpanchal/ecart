# Generated by Django 4.0.3 on 2022-04-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_rename_productdimensions_productimagedimensions'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_height',
            field=models.CharField(default='', max_length=24),
        ),
        migrations.AddField(
            model_name='product',
            name='product_width',
            field=models.CharField(default='', max_length=24),
        ),
    ]
