from django.db import models
from django.utils import timezone
# Create your models here.


class plano(models.Model):
    PER = (
        ('1', 'Avulsa'),
        ('2', 'Mensal'),
        ('2', 'Trimestral'),
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.DateTimeField(default=timezone.now)
    periodo = models.CharField(max_length=1, choices=PER)

    def __str__(self):
        return self.nome