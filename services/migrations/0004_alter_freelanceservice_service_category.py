# Generated by Django 3.2.4 on 2021-07-21 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20210721_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelanceservice',
            name='service_category',
            field=models.CharField(choices=[('Web, Mobile & Software Dev', (('DESKTOP', 'Desktop Software Development'), ('MOBILE', 'Mobile Development'), ('GAME', 'Game Development'), ('OTHER', 'Other Software Development'), ('TESTING', 'Testing'), ('UX', 'Web UX & Mobile Design'), ('WEB', 'Web Development'))), ('Design & Creative', (('ART', 'Art & Illustration'), ('AUDIO', 'Audio & Music Production'), ('VIDEO', 'Video & Animation'), ('DESIGN', 'Graphic, Editorial & Presentation Design'), ('ARTS', 'Performing Arts'), ('PHOTO', 'Photography'), ('BRANDING', 'Branding & Logo Design'), ('GAMING', 'Gaming AR/VR'))), ('Writing', (('CONTENT', 'Content & Copyright'), ('CREATIVE', 'Creative'), ('EDITING', 'Editing & Proofreading'), ('RESUMES', 'Resumes & Cover Letters'), ('TECHNICAL', 'Technical Writing'))), ('Translation', (('GENERAL', 'General'), ('LEGAL', 'Legal'), ('MEDICAL', 'Medical'), ('TECHNICAL', 'Technical')))], max_length=80),
        ),
    ]
