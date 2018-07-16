from django.shortcuts import render
from django.utils import timezone
from .models import agendamento
from paciente.models import paciente
from outro.models import professor

# Create your views here.
def agenda(request):
    if request.user.is_authenticated():
        hoje = timezone.now().strftime('%d de %B de %Y')
        dia = timezone.now().strftime('%a')
        agenda_data = timezone.now().strftime('%Y-%m-%d')
        professores = professor.objects.all().order_by('nome')
        agendas = agendamento.objects.filter(data__contains=agenda_data)
        return render(request, 'agenda.html', {'title':'Agenda', 'hoje':hoje, 'dia':dia, 'professores':professores, 'agendas':agendas})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def novo(request):
    if request.user.is_authenticated():
        pacientes = paciente.objects.all().order_by('nome')
        professores = professor.objects.all().order_by('nome')
        if request.method == 'POST':
            pac_id = request.POST.get('pac')
            pac = paciente.objects.filter(id=pac_id).get()
            prof_id = request.POST.get('prof')
            prof = professor.objects.filter(id=prof_id).get()
            horario = request.POST.get('hora')
            dia = request.POST.get('dia')
            return render(request, 'novo_1.html', {'title':'Novo Agendamento', 'pac':pac})
        return render(request, 'novo.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})