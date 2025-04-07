
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('', include('servicos.urls')),
    path('', include('sobre.urls')),
    path('', include('contato.urls')),
    path('admin/', admin.site.urls),
]