# Generated by Django 3.2.4 on 2021-08-10 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default='2021-08-10', verbose_name='date of birth'),
        ),
    ]
