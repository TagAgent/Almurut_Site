# Generated by Django 5.1 on 2024-10-02 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='favourite_products',
            field=models.ManyToManyField(to='market.product'),
        ),
    ]
