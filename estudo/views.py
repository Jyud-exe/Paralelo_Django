from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def ver_produtos(request):
    if request.method == "POST":
        nome = request.POST.get('usuario')
        if not nome:
            nome = 'Anônimo'
        mensagem = request.POST.get('mensagem')
        form = User(nome=nome, mensagem=mensagem)
        form.save()
        return HttpResponse('Fui chamado!')
    return render(request, 'index.html')

def catalogo(request):
    return render(request, 'catalogo.html')