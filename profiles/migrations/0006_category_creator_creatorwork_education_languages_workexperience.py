# Generated by Django 3.2.4 on 2021-07-09 08:24

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20210707_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[(None, 'Select Your Speciality'), ('Web, Mobile & Software Dev', (('DESKTOP', 'Desktop Software Development'), ('MOBILE', 'Mobile Development'), ('GAME', 'Game Development'), ('OTHER', 'Other Software Development'), ('TESTING', 'Testing'), ('UX', 'Web UX & Mobile Design'), ('WEB', 'Web Development'))), ('Design & Creative', (('DESKTOP', 'Desktop Software Development'),)), ('Writing', (('DESKTOP', 'Desktop Software Development'),)), ('Translation', (('DESKTOP', 'Desktop Software Development'),))], default='DE', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('profile', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile', serialize=False, to='profiles.userprofile')),
                ('town_or_city', models.CharField(max_length=70)),
                ('postcode', models.CharField(max_length=70)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=70)),
                ('work_town_or_city', models.CharField(max_length=70)),
                ('work_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('job_title', models.CharField(max_length=70)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('currently_working_here', models.BooleanField(blank=True, default=False, null=True)),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_workex', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_proficiency', models.IntegerField(choices=[(1, 'Basic'), (2, 'Conversational'), (3, 'Fluent'), (4, 'Native Bilingual')], default=3)),
                ('language', models.CharField(blank=True, max_length=70, null=True)),
                ('language_proficiency', models.IntegerField(choices=[(1, 'Basic'), (2, 'Conversational'), (3, 'Fluent'), (4, 'Native Bilingual')], default=3)),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_lang', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=70)),
                ('area_of_study', models.CharField(max_length=70)),
                ('qualification', models.CharField(max_length=70)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_ed', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='CreatorWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=70)),
                ('expertise_level', models.IntegerField(choices=[(1, 'Entry'), (2, 'Intermediate'), (3, 'Expert')], default=1)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.category')),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_work', to='profiles.userprofile')),
            ],
        ),
    ]
