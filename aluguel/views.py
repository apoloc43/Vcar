# Create your views here.
from django.shortcuts import render, redirect
from .models import Carro, Aluguel,Cliente
from .forms import AluguelForm

# Create your views here.

def index(request):
    carros = Carro.objects.all()[:5]
    return render(request, 'index.html', {"carros":carros})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/listar.html', {"clientes":clientes})

def listar_alugueis(request):
    alugueis = Aluguel.objects.all()
    return render(request, 'aluguel/listar.html', {"alugueis":alugueis})
    

def lista_carros(request):
    carros = Carro.objects.all()
    return render(request, 'carro/listar.html', {"carros":carros})

def detalhar_carro(request, pk):
    carro = Carro.objects.get(pk=pk)
    return render(request, 'carro/detalhar.html', {"carro":carro})

def realizar_aluguel(request):
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AluguelForm()
            return render(request, "aluguel/cadastrar.html", {'form': form})
    else:
        form = AluguelForm()
        return render(request, "aluguel/cadastrar.html", {'form': form})

def realizar_aluguel_carro(request, carro_pk):
    carro = Carro.objects.get(pk=carro_pk)
    aluguel = Aluguel()
    aluguel.carro = carro
    
    form = AluguelForm(instance=aluguel)
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AluguelForm(instance=aluguel)
            return render(request, "aluguel/cadastrar.html", {'form': form})
    else:
        form = AluguelForm(instance=aluguel)
        return render(request, "aluguel/cadastrar.html", {'form': form})