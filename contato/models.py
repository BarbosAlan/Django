from django.db import models

class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    email = models.EmailField(max_length=255)
    assunto = models.TextField(max_length=300)
    mensagem = models.TextField(max_length=300)

    def __str__(self):
        return self.nome
