from django.db import models
from paciente.models import paciente
from outro.models import professor
from django.utils import timezone

# Create your models here.
class agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(paciente, on_delete=models.CASCADE)
    hora = models.CharField(max_length=5)
    data = models.CharField(max_length=10)
    prof1 = models.ForeignKey(professor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.aluno