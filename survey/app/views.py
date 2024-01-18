from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import SurveyChoice, SurveyQuestion, SurveyEntry

def base(request):
    context = {'choices':SurveyChoice.objects.all(),
               'questions':SurveyQuestion.objects.all()}

    if request.method == 'POST':
        process_entry(request)
        return HttpResponseRedirect(reverse('completed'))

    return render(request, 'base.html', context)

def completed(request):
    return render(request, 'completed.html')

def process_entry(request, entry={}):
    questions = SurveyQuestion.objects.all()

    for i, question in enumerate(questions):
        entry[question.val] = request.POST.get(question.val)

    entry = SurveyEntry(answers=entry)
    entry.save()
