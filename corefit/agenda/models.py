from django.db import models
from paciente.models import paciente
from outro.models import professor
from django.utils import timezone
# Create your models here.
class agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(paciente)
    horario = models.DateTimeField()
    prof1 = models.ForeignKey(professor)
    
    def __str__(self):
        return self.aluno