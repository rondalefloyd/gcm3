from django.contrib import admin
from .models import SurveyEntry, SurveyQuestion, SurveyChoice

# Register your models here.
admin.site.register(SurveyEntry)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyChoice)