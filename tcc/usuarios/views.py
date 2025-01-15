from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import UsuarioPersonalizadoCreationForm, UsuarioPersonalizadoAuthenticationForm



# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        print(request.POST)
        form = UsuarioPersonalizadoCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            print(user)
            return redirect('polls:login')
            
    else:
         form = UsuarioPersonalizadoCreationForm() 
    return render(request, 'usuarios/cadastro.html', {'form': form})
       # else:
          #  nome= request.POST.get('nome')
           # CPF= request.POST.get('CPF')
            #email= request.POST.get('email')
            #senha= request.POST.get('senha')
       
     
    #user = User.objects.filter(nome=nome).first()
    #if user:
     #   return HttpResponse('Já existe um usuario com este nome')
    
   # user = User.objects.create_user(nome=nome, CPF=CPF, email=email, senha=senha,)

    #return HttpResponse (nome)

def user_login(request):
    if request.method =='POST':
      form = UsuarioPersonalizadoAuthenticationForm(request, request.POST)
      if form.is_valid():
          username = form.cleaned_data['usename']
          password = form.cleaned_data['password']
          user = authenticate(request, username=username, password=password)

          if user is not None:
              login(request, user)
              return redirect('polls:index')
        
    else:
        form = UsuarioPersonalizadoCreationForm() 
        return render(request, 'usuarios/cadastro.html', {'form': form})
   