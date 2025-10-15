from django.shortcuts import render
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
    return render(request, 'index.html')

def catalogo(request):
    if request.method == "POST":
        nome = request.POST.get('usuario')
        if not nome:
            nome = 'Anônimo'
        mensagem = request.POST.get('mensagem')
        form = User(nome=nome, mensagem=mensagem)
        form.save()
    return render(request, 'catalogo.html')