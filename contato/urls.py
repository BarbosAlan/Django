from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.contato, name='contato'),
    path('gravar/', views.gravar, name='gravar'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
