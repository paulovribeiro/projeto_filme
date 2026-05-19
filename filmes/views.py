from django.shortcuts import render

filmes = [
    {
        'id': 1,
        'titulo': 'Interestelar',
        'categoria': 'Ficção Científica',
        'descricao': 'Uma viagem pelo espaço em busca de um novo lar.',
        'autor': 'Christopher Nolan',
        'data': '2014'
    },
    {
        'id': 2,
        'titulo': 'Batman Begins',
        'categoria': 'Ação',
        'descricao': 'A origem do Batman.',
        'autor': 'Christopher Nolan',
        'data': '2005'
    },
    {
        'id': 3,
        'titulo': 'Vingadores Ultimato',
        'categoria': 'Super-herói',
        'descricao': 'A batalha final contra Thanos.',
        'autor': 'Marvel Studios',
        'data': '2019'
    }
]

def home(request):
    return render(request, 'filmes/home.html')

def lista_filmes(request):
    return render(request, 'filmes/lista.html', {'filmes': filmes})

def detalhe_filme(request, id):
    filme = next((f for f in filmes if f['id'] == id), None)

    return render(request, 'filmes/detalhes.html', {'filme': filme})