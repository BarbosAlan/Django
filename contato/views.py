from django.shortcuts import render, redirect
from contato.models import Pessoa

def contato(request):
    contexto = {
        'titulo': 'Whitepace | Contato',
        'h1': "Whitepace",
        'p': "Construa a sua marca, conquiste o mundo sem a habilidades de códigos ou designer necessários",
        'button': "Entrar em contato",
        'link': "/contato/",
        'pessoas': Pessoa.objects.all()
    }
    return render(request, 'contato/index.html', contexto)

def gravar(request):
    if request.method == "POST":
        nova_pessoa = Pessoa()
        nova_pessoa.nome = request.POST.get('nome')
        nova_pessoa.email = request.POST.get('email')
        nova_pessoa.assunto = request.POST.get('assunto')
        nova_pessoa.mensagem = request.POST.get('mensagem')
        nova_pessoa.save()
    return redirect('contato')
