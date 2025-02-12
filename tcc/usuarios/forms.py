from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext as _
from . models import MyModel, UsuarioPersonalizado
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UsuarioPersonalizadoCreationForm(UserCreationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['nome', 'email', 'CPF', 'password1', 'password2']


class UsuarioPersonalizadoAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

