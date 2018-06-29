from django.db import models
from outro.models import professor
from plano.models import plano

# Create your models here.
class paciente(models.Model):
    OPCAO = (
        ('1', 'Sim'),
        ('2', 'Nao'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    data_nasc = models.DateField(null=True, blank=True, default=False)
    data_venc = models.DateField(null=True, blank=True, default=False)
    queixa = models.CharField(max_length=500, null=True, blank=True)
    objetivo = models.CharField(max_length=500, null=True, blank=True)
    ativo = models.CharField(max_length=1, choices=OPCAO)
    prof1 = models.ForeignKey(professor)
    plan1 = models.ForeignKey(plano)

    def __str__(self):
        return self.nome