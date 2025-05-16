from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import register, custom_login

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('servicos/', include('servicos.urls')),
    path('sobre/', include('sobre.urls')),
    path('contato/', include('contato.urls')),
    
    # URLs de autenticação customizadas
    path('accounts/login/', custom_login, name='login'),
    path('accounts/register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),  # Para logout e password reset
    
    path('admin/', admin.site.urls),
]