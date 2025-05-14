
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('servicos/', include('servicos.urls')),
    path('sobre/', include('sobre.urls')),
    path('contato/', include('contato.urls')),
    path('admin/', admin.site.urls),
]

#Adicione URLs de autenticação de site Django (para login, logout, gerenciamento de senha)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
