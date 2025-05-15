from django.shortcuts import render, redirect
from django.contrib import messages
from contato.models import Pessoa

def contato(request):
    contexto = {
        'titulo': 'Whitepace | Contato',
        'h1': "Whitepace",
        'p': "Construa a sua marca, conquiste o mundo sem habilidades de códigos ou designer necessários",
        'button': "Entrar em contato",
        'link': "/contato/",
        'pessoas': Pessoa.objects.all().order_by('-id_pessoa')[:10]  # Mostra apenas os 10 mais recentes
    }
    return render(request, 'contato/index.html', contexto)

def gravar(request):
    if request.method == 'POST':
        try:
            nova_pessoa = Pessoa(
                nome=request.POST.get('nome'),
                email=request.POST.get('email'),
                assunto=request.POST.get('assunto'),
                mensagem=request.POST.get('mensagem')
            )
            nova_pessoa.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao enviar mensagem: {str(e)}')
    
    return redirect('contato')  # Redireciona para a página de contato