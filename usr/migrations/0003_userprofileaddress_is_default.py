# Generated by Django 4.0.3 on 2022-04-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr', '0002_userprofilewishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileaddress',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]