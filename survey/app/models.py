from django.db import models

# Create your models here.
class SurveyChoice(models.Model):
    choice = models.TextField()
    val = models.CharField(max_length=999)
    pass
class SurveyQuestion(models.Model):
    question = models.TextField()
    val = models.CharField(max_length=999)
    pass
class SurveyEntry(models.Model):
    answers = models.JSONField()