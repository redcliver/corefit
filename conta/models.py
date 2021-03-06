from django.db import models
from django.utils import timezone
# Create your models here.


class conta(models.Model):
    ESTADO = (
        ('1', 'Em Aberto'),
        ('2', 'Paga'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    data_reg = models.DateTimeField(default=timezone.now)
    data_venc = models.DateTimeField()
    data_pag = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADO)
    
    def __str__(self):
        return self.nome