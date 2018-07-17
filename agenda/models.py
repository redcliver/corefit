from django.db import models
from paciente.models import paciente
from outro.models import professor
from django.utils import timezone

# Create your models here.
class agendamento(models.Model):
    PRE = (
        ('0', 'Nao'),
        ('1', 'Sim'),
    )
    id = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(paciente, on_delete=models.CASCADE)
    data = models.DateTimeField()
    prof1 = models.ForeignKey(professor, on_delete=models.CASCADE)
    presenca = models.CharField(max_length=1, choices=PRE, default=0)
    
    def __str__(self):
        return self.aluno

class agendamento_2(models.Model):
    PRE = (
        ('0', 'Nao'),
        ('1', 'Sim'),
    )
    id = models.AutoField(primary_key=True)
    alunos = models.ManyToManyField(paciente)
    data = models.DateTimeField()
    prof1 = models.ForeignKey(professor, on_delete=models.CASCADE)
    presenca = models.CharField(max_length=1, choices=PRE, default=0)
    
    def __str__(self):
        return self.str(id)