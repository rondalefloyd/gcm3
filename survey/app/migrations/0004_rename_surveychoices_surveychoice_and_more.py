# Generated by Django 5.0.1 on 2024-01-18 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_surveyitem_surveyentry'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SurveyChoices',
            new_name='SurveyChoice',
        ),
        migrations.RenameModel(
            old_name='SurveyQuestions',
            new_name='SurveyQuestion',
        ),
    ]
