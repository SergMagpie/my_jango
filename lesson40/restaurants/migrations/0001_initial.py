# Generated by Django 3.2.4 on 2021-06-10 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('specialization', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50)),
                ('web_site', models.CharField(blank=True, max_length=25)),
                ('telephone_number', models.CharField(max_length=25)),
            ],
        ),
    ]
