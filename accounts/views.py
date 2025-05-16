from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registro realizado com sucesso!')
            return redirect('home')
        
        # Se o formulário não for válido, vamos renderizar o login.html com os erros
        login_form = AuthenticationForm()
        return render(request, 'registration/login.html', {
            'form': login_form,
            'register_form': form
        })
    
    return redirect('login')

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
        
        # Se o login falhar, mostre os erros
        register_form = RegisterForm()
        return render(request, 'registration/login.html', {
            'form': form,
            'register_form': register_form
        })
    
    # Se for GET, mostre o formulário vazio
    form = AuthenticationForm()
    register_form = RegisterForm()
    return render(request, 'registration/login.html', {
        'form': form,
        'register_form': register_form
    })