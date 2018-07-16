from django.db import models
from outro.models import professor
from plano.models import plano
from django.utils import timezone

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
    prof1 = models.ForeignKey(professor, null=True)
    plan1 = models.ForeignKey(plano, null=True)

    def __str__(self):
        return self.nome

class pagamento(models.Model):
    id = models.AutoField(primary_key=True)
    data_pag = models.DateField(default=timezone.now)

    def __int__(self):
        return self.id