from django.shortcuts import render
from django.utils import timezone
from agenda.models import agendamento
from paciente.models import paciente
from outro.models import professor

# Create your views here.
def agenda(request):
    if request.user.is_authenticated():
        hoje = timezone.now().strftime('%d de %B de %Y')
        dia = timezone.now().strftime('%a')
        
        return render(request, 'agenda.html', {'title':'Agenda', 'hoje':hoje, 'dia':dia})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def novo(request):
    if request.user.is_authenticated():
        pacientes = paciente.objects.all()
        professores = professor.objects.all().order_by('nome')
        return render(request, 'novo.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})