from django.urls import path
from . import views
from django.contrib import admin

app_name = "usuarios"

urlpatterns = [
    path('admin/', admin.site.urls),  # Apenas necessário no arquivo principal de URLs
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login, name="login"),
]
