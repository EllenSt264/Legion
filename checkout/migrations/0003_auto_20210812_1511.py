# Generated by Django 3.2.4 on 2021-08-12 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_auto_20210810_2256'),
        ('checkout', '0002_remove_orderlineitem_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPackage',
            fields=[
                ('service', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='services.service')),
                ('enable_all_packages', models.BooleanField(default=True)),
                ('package_title', models.CharField(max_length=90)),
                ('package_description', models.TextField()),
                ('client_requirements', models.TextField(blank=True, null=True)),
                ('delivery_time', models.IntegerField(choices=[(1, 'One Day'), (2, 'Two Day'), (3, 'Three Day'), (4, 'Four Day'), (5, 'Five Day'), (6, 'Six Day'), (7, 'Seven Day'), (12, 'Twelve Day'), (14, 'Two Week'), (21, 'Three Week'), (30, 'One Month')])),
                ('revisions', models.IntegerField(choices=[(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (6, 'Six'), (7, 'Seven'), (8, 'Eight')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fast_delivery_time', models.IntegerField(blank=True, choices=[(1, 'One Day'), (2, 'Two Day'), (3, 'Three Day'), (4, 'Four Day'), (5, 'Five Day'), (6, 'Six Day'), (7, 'Seven Day'), (12, 'Twelve Day'), (14, 'Two Week'), (21, 'Three Week'), (30, 'One Month')], null=True)),
                ('fast_delivery_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('reference_images', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='package',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='package', to='checkout.orderpackage'),
            preserve_default=False,
        ),
    ]
