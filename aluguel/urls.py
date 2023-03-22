"""carro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import index, lista_carros, realizar_aluguel, detalhar_carro, realizar_aluguel_carro,listar_clientes,listar_alugueis
from .views import cadastrar_carro,detalhar_cliente,atualizar_carro,deletar_carro

urlpatterns = [
    path('', index, name='index'),
    path('carros/', lista_carros, name='listar_carros'),
    path('alugueis/', listar_alugueis, name='listar_alugueis'),
    path('carro/cadastrar', cadastrar_carro, name='cadastrar_carro'),
    path('carro/atualizar/<int:pk>', atualizar_carro, name='atualizar_carro'),
    
    
    path('carro/deletar/<int:pk>', deletar_carro, name='deletar_carro'),
    path('cliente/', listar_clientes, name='listar_clientes'),
    path('cliente/<int:pk>', detalhar_cliente, name='detalhar_cliente'),
    path('carros/<int:pk>', detalhar_carro, name='detalhar_carro'),
    path('carros/aluguel/<int:carro_pk>', realizar_aluguel_carro, name='realizar_aluguel_carro' ),
    path('aluguel/add', realizar_aluguel, name='realizar_aluguel'),
]
