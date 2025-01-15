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
    if request.method == "GET":
        return render(request, 'polls/cadastro.html')
    else:
        nome= request.POST.get('nome')
        CPF= request.POST.get('CPF')
        email= request.POST.get('email')
        senha= request.POST.get('senha')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        CEP = request.POST.get(' CEP')
        estado = request.POST.get('Estado')


def debate(request):
    return render(request, 'polls/debate.html')




    