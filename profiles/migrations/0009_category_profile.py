# Generated by Django 3.2.4 on 2021-07-10 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_category_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_cat', to='profiles.userprofile'),
        ),
    ]
