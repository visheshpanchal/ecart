# Generated by Django 4.0 on 2022-02-22 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_authmodel_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authmodel',
            name='is_staff',
        ),
    ]
