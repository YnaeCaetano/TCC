from django.db import models
from .validators import validate_cpf
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from cpf_field.models import CPFField

# Create your models here.

class UsuarioPersonalizadoManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Você não informou um emai válido')
        email =  self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff' , True)
        extra_fields.setdefault('is_superuser', True)
        

        return self.create_user(email, password, **extra_fields)
    
class UsuarioPersonalizado(AbstractUser, PermissionsMixin):
    username = None
    nome = models.CharField(max_length= 50, blank= True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    CPF = CPFField('CPF')
    is_active = models.BooleanField (default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioPersonalizadoManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class CPFField(models.CharField):
    default_validators = [validate_cpf]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 14)
        super().__init__(*args, **kwargs)


class MyModel(models.Model):
    cpf = CPFField('CPF')