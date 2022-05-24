from os import path

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = path.join('polls', 'index.html')
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last published questions."""
        question_amount = 5
        return Question.objects.order_by('-pub_date')[:question_amount]


class DetailView(generic.DetailView):
    model = Question
    template_name = path.join('polls', 'detail.html')


class ResultsView(generic.DetailView):
    model = Question
    template_name = path.join('polls', 'results.html')


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            'polls/detail.html',
            {
                'question': question,
                'error_message': "You didn't select a choice.",
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse(
            'polls:results',
            args=(question.id,)
        ))
