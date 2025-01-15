from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("index", views.index, name="index"),
    # ex: /polls/5/
    path("login", views.login, name="login"),

    path("sobre", views.sobre, name="sobre"),

    path("marketplace", views.marketplace, name="marketplace"),

    path("eventos", views.eventos, name="eventos"),

    path("cadastro", views.cadastro, name="cadastro"),

    path("debate", views.debate, name="debate"),


]