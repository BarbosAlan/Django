from django.shortcuts import render

from contato.models import Pessoa

# Create your views here.

def contato(request):
    contexto = {
        'titulo' : 'Whitepace | Contato',
        'h1':"Whitepace",
        'p': "Construa a sua marca, cosquite o mundo sem a habilidades de códigos ou designer necessários",
        'button': "Entrar em contato",
        'link': "/contato/",
        'pessoas' : Pessoa.objects.all()
    }
    return render(request,
                  'contato/index.html',
                  contexto,)

def gravar(request):
    nova_pessoa = Pessoa()
    nova_pessoa.nome = request.POST.get('nome')
    nova_pessoa.email = request.POST.get('email')
    nova_pessoa.assunto = request.POST.get('assunto')
    nova_pessoa.mensagem = request.POST.get('mensagem')
    nova_pessoa.save()
    
    return contato(request)