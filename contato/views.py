from django.shortcuts import render

from contato.models import Pessoa

# Create your views here.

def cadastro(request):
    contexto = {
        'titulo' : 'Jornada Viagem | Cadastro',
        'pessoas' : Pessoa.objects.all()
    }
    return render(request,
                  'cadastro/index.html',
                  contexto,)

def gravar(request):
    nova_pessoa = Pessoa()
    nova_pessoa.nome = request.POST.get('nome')
    nova_pessoa.email = request.POST.get('email')
    nova_pessoa.assunto = request.POST.get('assunto')
    nova_pessoa.mensagem = request.POST.get('mensagem')
    nova_pessoa.save()
    
    return cadastro(request)