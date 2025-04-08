from django.shortcuts import render

# Create your views here.

def home(request):
    contexto = {
        'titulo' : 'Whitepace | home',
        'h1':"Whitepace",
        'p': "Construa a sua marca, cosquite o mundo sem a habilidades de códigos ou designer necessários",
        'button': "Entrar em contato",
        'link': "/contato/"
    }
    return render(request, 
                  'home/index.html',
                  contexto,)