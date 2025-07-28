from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from calculadora.views import login_view, registrar, calculos

urlpatterns = [
    path('admin/',    admin.site.urls),
    path('',          login_view,   name='login'),       # raiz → login
    path('registrar/',registrar,     name='registrar'),   # cadastro
    path('sair/',     LogoutView.as_view(next_page='login'),
                                               name='sair'),
    path('calculadora/', calculos,   name='calculos'),    # calculadora após login
]
