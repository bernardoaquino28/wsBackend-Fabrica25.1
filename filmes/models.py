from django.db import models

class Filme(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20)
    duracao = models.IntegerField()
    preco = models.IntegerField()

    class Meta:
        app_label = 'filmes'
        
class Buscar(models.Model):
    nome_filme = models.CharField(max_length=50)
    

    
    def __str__(self):
        return self.nome
