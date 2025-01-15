from django import forms
from . models import UsuarioPersonalizado
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UsuarioPersonalizadoCreationForm(UserCreationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['nome', 'email', 'cpf', 'password1', 'password2']

class UsuarioPersonalizadoAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
