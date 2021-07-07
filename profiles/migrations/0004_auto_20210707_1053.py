# Generated by Django 3.2.4 on 2021-07-07 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20210706_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_recruiter',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='recruiter',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.recruiter', verbose_name='Recruiter'),
        ),
    ]
