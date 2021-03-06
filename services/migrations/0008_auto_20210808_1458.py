# Generated by Django 3.2.4 on 2021-08-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20210808_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='premiumpackage',
            old_name='client_requirements',
            new_name='premium_client_requirements',
        ),
        migrations.RenameField(
            model_name='premiumpackage',
            old_name='fast_delivery_time',
            new_name='premium_delivery_time',
        ),
        migrations.RenameField(
            model_name='premiumpackage',
            old_name='fast_delivery_price',
            new_name='premium_fast_delivery_price',
        ),
        migrations.RenameField(
            model_name='premiumpackage',
            old_name='reference_images',
            new_name='premium_reference_images',
        ),
        migrations.RenameField(
            model_name='standardpackage',
            old_name='client_requirements',
            new_name='standard_client_requirements',
        ),
        migrations.RenameField(
            model_name='standardpackage',
            old_name='fast_delivery_time',
            new_name='standard_delivery_time',
        ),
        migrations.RenameField(
            model_name='standardpackage',
            old_name='fast_delivery_price',
            new_name='standard_fast_delivery_price',
        ),
        migrations.RenameField(
            model_name='standardpackage',
            old_name='reference_images',
            new_name='standard_reference_images',
        ),
        migrations.RemoveField(
            model_name='basicpackage',
            name='details',
        ),
        migrations.RemoveField(
            model_name='premiumpackage',
            name='delivery_time',
        ),
        migrations.RemoveField(
            model_name='premiumpackage',
            name='details',
        ),
        migrations.RemoveField(
            model_name='premiumpackage',
            name='package_description',
        ),
        migrations.RemoveField(
            model_name='premiumpackage',
            name='package_title',
        ),
        migrations.RemoveField(
            model_name='premiumpackage',
            name='price',
        ),
        migrations.RemoveField(
            model_name='premiumpackage',
            name='revisions',
        ),
        migrations.RemoveField(
            model_name='standardpackage',
            name='delivery_time',
        ),
        migrations.RemoveField(
            model_name='standardpackage',
            name='details',
        ),
        migrations.RemoveField(
            model_name='standardpackage',
            name='package_description',
        ),
        migrations.RemoveField(
            model_name='standardpackage',
            name='package_title',
        ),
        migrations.RemoveField(
            model_name='standardpackage',
            name='price',
        ),
        migrations.RemoveField(
            model_name='standardpackage',
            name='revisions',
        ),
        migrations.AddField(
            model_name='premiumpackage',
            name='premium_fast_delivery_time',
            field=models.IntegerField(blank=True, choices=[(1, 'One Day'), (2, 'Two Day'), (3, 'Three Day'), (4, 'Four Day'), (5, 'Five Day'), (6, 'Six Day'), (7, 'Seven Day'), (12, 'Twelve Day'), (14, 'Two Week'), (21, 'Three Week'), (30, 'One Month')], null=True),
        ),
        migrations.AddField(
            model_name='premiumpackage',
            name='premium_package_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='premiumpackage',
            name='premium_package_title',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='premiumpackage',
            name='premium_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='premiumpackage',
            name='premium_revisions',
            field=models.IntegerField(blank=True, choices=[(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (6, 'Six'), (7, 'Seven'), (8, 'Eight')], null=True),
        ),
        migrations.AddField(
            model_name='standardpackage',
            name='standard_fast_delivery_time',
            field=models.IntegerField(blank=True, choices=[(1, 'One Day'), (2, 'Two Day'), (3, 'Three Day'), (4, 'Four Day'), (5, 'Five Day'), (6, 'Six Day'), (7, 'Seven Day'), (12, 'Twelve Day'), (14, 'Two Week'), (21, 'Three Week'), (30, 'One Month')], null=True),
        ),
        migrations.AddField(
            model_name='standardpackage',
            name='standard_package_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='standardpackage',
            name='standard_package_title',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='standardpackage',
            name='standard_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='standardpackage',
            name='standard_revisions',
            field=models.IntegerField(blank=True, choices=[(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (6, 'Six'), (7, 'Seven'), (8, 'Eight')], null=True),
        ),
    ]
