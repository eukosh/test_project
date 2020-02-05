from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question


def index(request):
    questions = Question.objects.order_by('-pub_date')[:5]
    context = {
        'questions_list': questions,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    context = {
        'question': question,
        'choices': choices,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = f'You are looking at the results of question {question_id}.'
    return HttpResponse(response)


def vote(request, question_id):
    response = f'You are voting on question {question_id}.'
    return HttpResponse(response)
