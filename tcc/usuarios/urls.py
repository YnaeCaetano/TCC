from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = "usuarios"

urlpatterns = [
    path('admin/', admin.site.urls),  # Apenas necessário no arquivo principal de URLs
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.user_login, name="login"),
    path('sair/', views.sair, name="sair"),
    path ('password_change', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done,', auth_views.PasswordChangeDoneView.as_view(), name='password-change_done')
]
