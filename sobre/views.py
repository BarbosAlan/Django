from django.shortcuts import render

# Create your views here.
def sobre(request):
    contexto = {
        'titulo' : 'Whitepace | Sobre'
    }
    return render(request, 
                  'sobre/index.html',
                  contexto,)