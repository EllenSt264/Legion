# Generated by Django 3.2.4 on 2021-08-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20210812_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='delivery_cost',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
