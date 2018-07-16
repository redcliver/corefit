from django.shortcuts import render
from django.utils import timezone
from .models import agendamento
from paciente.models import paciente
from outro.models import professor
from plano.models import plano

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
        planos = plano.objects.all().order_by('nome')
        dia = timezone.now().strftime('%w')
        d = timezone.now().strftime('%d')
        m = timezone.now().strftime('%m')
        if request.method == 'POST':
            pac_id = request.POST.get('pac')
            pac = paciente.objects.filter(id=pac_id).get()
            prof_id = request.POST.get('prof')
            prof = professor.objects.filter(id=prof_id).get()
            horario = request.POST.get('hora')
            dia = request.POST.get('dia')
            novo_age = agendamento(aluno=pac, prof1=prof, hora=horario, data=dia)
            novo_age.save()
            msg = "Paciente agendado com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        if dia == '1':
            d1 = str(d)+"/"+str(m)
            d2 = str(int(d)+1)+"/"+str(m)
            d3 = str(int(d)+2)+"/"+str(m)
            d4 = str(int(d)+3)+"/"+str(m)
            d5 = str(int(d)+4)+"/"+str(m)
            
            return render(request, 'novo.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '2':
            d1 = str(int(d)-1)+"/"+str(m)
            d2 = str(d)+"/"+str(m)
            d3 = str(int(d)+1)+"/"+str(m)
            d4 = str(int(d)+2)+"/"+str(m)
            d5 = str(int(d)+3)+"/"+str(m)
            
            return render(request, 'novo.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '3':
            d1 = str(int(d)-2)+"/"+str(m)
            d2 = str(int(d)-1)+"/"+str(m)
            d3 = str(d)+"/"+str(m)
            d4 = str(int(d)+1)+"/"+str(m)
            d5 = str(int(d)+2)+"/"+str(m)
            
            return render(request, 'novo.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '4':
            d1 = str(int(d)-3)+"/"+str(m)
            d2 = str(int(d)-2)+"/"+str(m)
            d3 = str(int(d)-1)+"/"+str(m)
            d4 = str(d)+"/"+str(m)
            d5 = str(int(d)+1)+"/"+str(m)
            
            return render(request, 'novo.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '5':
            d1 = str(int(d)-4)+"/"+str(m)
            d2 = str(int(d)-3)+"/"+str(m)
            d3 = str(int(d)-2)+"/"+str(m)
            d4 = str(int(d)-1)+"/"+str(m)
            d5 = str(d)+"/"+str(m)
            
            return render(request, 'novo.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})