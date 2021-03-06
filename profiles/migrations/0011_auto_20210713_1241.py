# Generated by Django 3.2.4 on 2021-07-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_remove_creatorwork_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='area_of_study',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='institution_name',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='qualification',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='languages',
            name='language_proficiency',
            field=models.IntegerField(blank=True, choices=[(1, 'Basic'), (2, 'Conversational'), (3, 'Fluent'), (4, 'Native Bilingual')], default=3, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='company_name',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='job_title',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='work_town_or_city',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
