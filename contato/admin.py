from django.contrib import admin
from .models import Pessoa

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id_pessoa', 'nome', 'email', 'assunto')
    search_fields = ('nome', 'email', 'assunto')
    list_filter = ('assunto',)
