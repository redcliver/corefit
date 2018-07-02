from django.db import models

# Create your models here.

class teste(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='teste', blank=True)
    
    def __str__(self):
        return self.nome