from django.shortcuts import render

# Create your views here.
def servicos(request):
    contexto = {
        'titulo' : 'Whitepace | Servicos'
    }
    return render(request, 
                  'servicos/index.html',
                  contexto,)