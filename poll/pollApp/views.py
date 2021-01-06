from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import PollQuestion, Option
from django.urls import reverse


# Create your views here.

def index(request):

    return render(request, 'index.html')


def results(request):

    #question = pollQuestion.objects.get(pk=pollquestion_id)
    return render(request, 'results.html')

def vote(request):

    numberOfOptions = request.POST['sel']
    poll_question = PollQuestion.objects.create(title = request.POST['ti'])
    
    for i in range (numberOfOptions):
        item = 'cho'+str(i+1)
        poll_question.choice_set.create(option_text = request.POST[item] , votes=0)
    
    return render(request, 'vote.html', {'poll_question':poll_question, 'numberOfOptions':numberOfOptions})
