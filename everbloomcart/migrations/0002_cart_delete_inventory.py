# Generated by Django 4.1.7 on 2023-02-22 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everbloomcart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=250)),
                ('card', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]
