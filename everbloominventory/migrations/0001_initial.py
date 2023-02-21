# Generated by Django 4.1.7 on 2023-02-21 20:08

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
                ('product', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=250)),
                ('card', models.CharField(max_length=100)),
            ],
        ),
    ]