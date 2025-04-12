from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django import forms
from django.forms import modelform_factory

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # output = ", ".join([q.question_text for q in latest_question_list])
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     # return HttpResponse("You're looking at question %s." % question_id)
#     return render(request, "polls/detail.html", {"question": question})
        
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def crud(request):
    # return HttpResponse("You're looking at the crud page.")
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/crud.html", context)

def get_question_list(request):
    context = {}
    context['questions'] = Question.objects.all()
    return render(request, 'polls/partial/question_list.html', context)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = []

def add_question(request):
    context = {'form': QuestionForm()}
    return render(request, 'polls/partial/add_question.html', context)

def add_question(request):
    context = {}
    form = QuestionForm(request.POST)
    context['form'] = form
    if form.is_valid():
        context['question'] = form.save()
    else:
        return render(request, 'polls/partial/add_question.html', context)
    return render(request, 'polls/partial/question_row.html', context)

def cancel_add_question(request):
    return HttpResponse()

def delete_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    question.delete()
    return HttpResponse()

def edit_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {}
    context['question'] = question
    context['form'] = QuestionForm(initial={
        'question_text':question.question_text,
        'pub_date': question.pub_date,
        
    })
    return render(request, 'polls/partial/edit_question.html', context)

def edit_question_submit(request, question_id):
    context = {}
    question = Question.objects.get(pk=question_id)
    context['question'] = question
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'polls/partial/edit_question.html', context)
    return render(request, 'polls/partial/question_row.html', context)