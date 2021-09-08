from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils import timezone

class User(models.Model):
    nome = models.CharField(max_length=70)
    email = models.EmailField( max_length=254)

class Edicao(models.Model):
    edicao = models.CharField(max_length=50)

class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE)
    descricao = models.TextField()
    
    CATEGORIAS_CHOICES =[
        ('Sociedade', 'S'),
        ('Ciência', 'C'),
        ('Crime','CM'),
        ('Cultura','CL'),
        ('Economia','E'),
        ('Educação','ED'),
        ('Esporte', 'ES'),
        ('Política', 'P'),
        ('Saúde','S'),
    ]

    categoria = models.CharField( max_length=10, choices=CATEGORIAS_CHOICES, default= 'Sociedade')

class Comentario(models.Model):
    avaliacao = models.DecimalField(max_digits=1, decimal_places=1)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=300)
    data_publicação = models.DateField(auto_now=False, auto_now_add=True)
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE)
    
