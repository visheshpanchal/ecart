# Generated by Django 4.0.3 on 2022-03-26 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=65)),
                ('last_name', models.CharField(max_length=65)),
                ('email', models.EmailField(max_length=128)),
                ('phone_number', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('zip_number', models.CharField(max_length=6)),
                ('address_1', models.CharField(max_length=256)),
                ('address_2', models.CharField(max_length=256)),
            ],
        ),
    ]