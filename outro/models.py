from django.db import models
from django.utils import timezone
# Create your models here.

class professor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    data_nasc = models.DateField(default=timezone.now)

   