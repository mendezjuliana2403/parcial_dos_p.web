from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'modulo/index.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Comida
from .forms import ComidaForm
from django.contrib.auth.decorators import login_required

# LISTAR
@login_required
def lista_comidas(request):
    comidas = Comida.objects.all()
    return render(request, 'comidas/lista.html', {'comidas': comidas})

# DETALLE
@login_required
def detalle_comida(request, id):
    comida = get_object_or_404(Comida, id=id)
    return render(request, 'comidas/detalle.html', {'comida': comida})

# CREAR
@login_required
def crear_comida(request):
    if request.method == 'POST':
        form = ComidaForm(request.POST, request.FILES)
        if form.is_valid():
            comida = form.save(commit=False)
            comida.creado_por = request.user
            comida.save()
            return redirect('lista_comidas')
    else:
        form = ComidaForm()
    return render(request, 'comidas/form.html', {'form': form})


# EDITAR
@login_required
def editar_comida(request, id):
    comida = get_object_or_404(Comida, id=id)
    form = ComidaForm(request.POST or None, request.FILES or None, instance=comida)
    if form.is_valid():
        form.save()
        return redirect('lista_comidas')
    return render(request, 'comidas/form.html', {'form': form})


# ELIMINAR
@login_required
def eliminar_comida(request, id):
    comida = get_object_or_404(Comida, id=id)
    comida.delete()
    return redirect('lista_comidas')


# FUNCIONALIDAD EXTRA: BUSCADOR
@login_required
def buscar(request):
    query = request.GET.get('q')
    resultados = Comida.objects.filter(titulo__icontains=query)
    return render(request, 'comidas/lista.html', {'comidas': resultados})