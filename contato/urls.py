from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.contato, name='contato'),
    path('gravar/',views.gravar, name='gravar'),
]