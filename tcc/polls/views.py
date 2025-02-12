from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .models import Produto


def index(request):
    latest_question_list = Usuario.objects.all()
    context = {"latest_question_list": latest_question_list}
    return render(request, 'polls/index.html', context)

def login(request):
    return render(request, 'polls/login.html')


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

def teste(request):
    return render(request, 'polls/teste.html')

def perfil(request):
    return render(request, 'polls/perfil.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto

def produto_detalhe(request):
    return render(request, 'polls/produto_detalhe.html')

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    # Lógica para adicionar ao carrinho (exemplo: salvar na sessão)
    carrinho = request.session.get('carrinho', {})
    carrinho[produto_id] = {'nome': produto.nome, 'preco': str(produto.preco)}
    request.session['carrinho'] = carrinho
    return redirect('produto_detalhe', produto_id=produto.id)

def comprar(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    # Lógica de finalização da compra (exemplo: redirecionar para checkout)
    return redirect('checkout')

def carrinho(request):
    return render(request, 'polls/carrinho.html')

def remover_do_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})

    if str(produto_id) in carrinho:
        del carrinho[str(produto_id)]
        request.session['carrinho'] = carrinho

    return redirect('carrinho')

def checkout(request):
    return render(request, 'checkout.html')

    