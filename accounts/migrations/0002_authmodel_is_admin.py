# Generated by Django 4.0 on 2022-02-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authmodel',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]