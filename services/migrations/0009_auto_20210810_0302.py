# Generated by Django 3.2.4 on 2021-08-10 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20210808_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='faq_answer_1',
        ),
        migrations.RemoveField(
            model_name='service',
            name='faq_answer_2',
        ),
        migrations.RemoveField(
            model_name='service',
            name='faq_answer_3',
        ),
        migrations.RemoveField(
            model_name='service',
            name='faq_answer_4',
        ),
        migrations.RemoveField(
            model_name='service',
            name='faq_question_1',
        ),
        migrations.RemoveField(
            model_name='service',
            name='faq_question_2',
        ),
        migrations.RemoveField(
            model_name='service',
            name='faq_question_3',
        ),
        migrations.RemoveField(
            model_name='service',
            name='faq_question_4',
        ),
    ]
