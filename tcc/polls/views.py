from django.db.models import F
from django.shortcuts import render
from .models import Usuario



def index(request):
    latest_question_list = Usuario.objects.all()
    context = {"latest_question_list": latest_question_list}
    return render(request, 'polls/index.html', context)

def login(request):
    return render(request, 'polls/login.html')


def anna(request):
    return render(request, 'polls/anna.html')


def sobre(request):
    return render(request, 'polls/sobre.html')

def marketplace(request):
    return render(request, 'polls/marketplace.html')

def eventos(request):
    return render(request, 'polls/eventos.html')

def cadastro(request):
    return render(request, 'polls/cadastro.html')

def debate(request):
    return render(request, 'polls/debate.html')




    