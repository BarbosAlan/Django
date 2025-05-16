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
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redireciona para a home após registrar
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})
