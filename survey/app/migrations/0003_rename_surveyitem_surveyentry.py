# Generated by Django 5.0.1 on 2024-01-18 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_surveychoices_surveyquestions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SurveyItem',
            new_name='SurveyEntry',
        ),
    ]
