# Generated by Django 4.0.3 on 2022-03-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileWishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True)),
                ('product_ids', models.JSONField()),
            ],
        ),
    ]
