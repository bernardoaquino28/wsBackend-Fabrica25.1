import requests
from django.shortcuts import render, redirect
from .models import Filme
from .forms import FilmeForm,BuscarForm

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/lista.html', {'filmes': filmes})

def novo_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm()
    return render(request, 'filmes/novo.html', {'form': form})

def editar_filme(request, pk):
    filme = Filme.objects.get(pk=pk)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'filmes/editar.html', {'form': form})

def excluir_filme(request, pk):
    filme = Filme.objects.get(pk=pk)
    if request.method == 'POST':
        filme.delete()
        return redirect('lista_filmes')
    return render(request, 'filmes/excluir.html', {'filme': filme})

def buscar_filme_omdb(request):
    api_key = 'c7870484'
    form = BuscarForm() 
    if request.method == 'POST':
         
        nome_filme = request.POST.get('nome_filme')
        url = f'http://www.omdbapi.com/?apikey={api_key}&t={nome_filme}'
        response = requests.get(url)
        data = response.json()
        if data['Response'] == 'True':
            filme = Filme(nome=data['Title'], categoria=data['Genre'], duracao=0, preco=0)
            filme.save()
            return redirect('lista_filmes') 
            
    return render(request, 'filmes/buscar.html', {'form': form}) 
