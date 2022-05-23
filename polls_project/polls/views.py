from os import path

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question


def index(request):
    question_amount = 5
    template = path.join('polls', 'index.html')
    latest_question_list = Question.objects.order_by('-pub_date')[:question_amount]
    context = {'latest_question_list': latest_question_list}
    return render(request, template, context)


def detail(request, question_id):
    template = path.join('polls', 'detail.html')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, template, {'question': question})


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")