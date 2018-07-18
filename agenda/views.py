from django.shortcuts import render
from datetime import datetime, time
from django.utils import timezone
from .models import agendamento, agendamento_2
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
        prof = professor.objects.first()
        agendas = agendamento.objects.filter(data__icontains=agenda_data, prof1=prof).order_by('data')
        if request.POST.get('data_busca') != None and request.POST.get('profissional') != None:
            data_bu = request.POST.get('data_busca')
            data_obj = datetime.strptime(''+data_bu+'', '%Y-%m-%d').date()
            dia = data_obj.strftime('%a')
            hoje = data_obj.strftime('%d de %B de %Y')
            pro = request.POST.get('profissional')
            prof = professor.objects.filter(id=pro).get()
            agendas = agendamento.objects.filter(data__icontains=data_obj, prof1=prof).order_by('data')
            return render(request, 'agenda.html', {'title':'Agenda', 'hoje':hoje, 'dia':dia, 'professores':professores, 'agendas':agendas, 'prof':prof})
        return render(request, 'agenda.html', {'title':'Agenda', 'hoje':hoje, 'dia':dia, 'professores':professores, 'agendas':agendas, 'prof':prof})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def novo(request):
    if request.user.is_authenticated():
        return render(request, 'novo.html', {'title':'Novo Agendamento'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def novo_11(request):
    if request.user.is_authenticated():
        pacientes = paciente.objects.all().order_by('nome')
        professores = professor.objects.all().order_by('nome')
        planos = plano.objects.all().order_by('nome')
        dia = timezone.now().strftime('%w')
        d = timezone.now().strftime('%d')
        m = timezone.now().strftime('%m')
        y = timezone.now().strftime('%Y')
        if request.method == 'POST' and request.POST.get('plan') == '2':
            pac_id = request.POST.get('pac')
            pac = paciente.objects.filter(id=pac_id).get()
            prof_id = request.POST.get('prof')
            prof = professor.objects.filter(id=prof_id).get()
            horario = request.POST.get('hora')
            dia = request.POST.get('dia')
            data_obj = datetime.strptime(''+y+' '+m+' '+dia+' '+horario+'', '%Y %m %d %H:%M')
            novo_age = agendamento(aluno=pac, prof1=prof, data=data_obj)
            novo_age.save()
            if data_obj.strftime('%w') == '1':
                data = "Segunda-Feira as "+horario+""  
                msg = "Paciente agendado com sucesso."
                return render(request, 'home/home.html', {'title':'Home', 'msg':msg, 'novo_age':novo_age, 'data':data})
            elif data_obj.strftime('%w') == '2':
                data = "Terca-Feira as "+horario+""  
                msg = "Paciente agendado com sucesso."
                return render(request, 'home/home.html', {'title':'Home', 'msg':msg, 'novo_age':novo_age, 'data':data})
            elif data_obj.strftime('%w') == '3':
                data = "Quarta-Feira as "+horario+""
                msg = "Paciente agendado com sucesso."
                return render(request, 'home/home.html', {'title':'Home', 'msg':msg, 'novo_age':novo_age, 'data':data})
            elif data_obj.strftime('%w') == '4':
                data = "Quinta-Feira as "+horario+"" 
                msg = "Paciente agendado com sucesso."
                return render(request, 'home/home.html', {'title':'Home', 'msg':msg, 'novo_age':novo_age, 'data':data})
            elif data_obj.strftime('%w') == '5':
                data = "Sexta-Feira as "+horario+""
                msg = "Paciente agendado com sucesso."
                return render(request, 'home/home.html', {'title':'Home', 'msg':msg, 'novo_age':novo_age, 'data':data})
            msg = "Paciente agendado com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg, 'novo_age':novo_age})
        if dia == '1':
            d1 = str(d)
            d2 = str(int(d)+1)
            d3 = str(int(d)+2)
            d4 = str(int(d)+3)
            d5 = str(int(d)+4)
            
            return render(request, 'novo_11.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5, 'm':m})
        if dia == '2':
            d1 = str(int(d)-1)
            d2 = str(d)
            d3 = str(int(d)+1)
            d4 = str(int(d)+2)
            d5 = str(int(d)+3)
            
            return render(request, 'novo_11.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5, 'm':m})
        if dia == '3':
            d1 = str(int(d)-2)
            d2 = str(int(d)-1)
            d3 = str(d)
            d4 = str(int(d)+1)
            d5 = str(int(d)+2)
            
            return render(request, 'novo_11.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5, 'm':m})
        if dia == '4':
            d1 = str(int(d)-3)
            d2 = str(int(d)-2)
            d3 = str(int(d)-1)
            d4 = str(d)
            d5 = str(int(d)+1)
            
            return render(request, 'novo_11.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5, 'm':m})
        if dia == '5':
            d1 = str(int(d)-4)
            d2 = str(int(d)-3)
            d3 = str(int(d)-2)
            d4 = str(int(d)-1)
            d5 = str(d)
            
            return render(request, 'novo_11.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5, 'm':m})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def novo_12(request):
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
            
            return render(request, 'novo_12.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '2':
            d1 = str(int(d)-1)+"/"+str(m)
            d2 = str(d)+"/"+str(m)
            d3 = str(int(d)+1)+"/"+str(m)
            d4 = str(int(d)+2)+"/"+str(m)
            d5 = str(int(d)+3)+"/"+str(m)
            
            return render(request, 'novo_12.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '3':
            d1 = str(int(d)-2)+"/"+str(m)
            d2 = str(int(d)-1)+"/"+str(m)
            d3 = str(d)+"/"+str(m)
            d4 = str(int(d)+1)+"/"+str(m)
            d5 = str(int(d)+2)+"/"+str(m)
            
            return render(request, 'novo_12.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '4':
            d1 = str(int(d)-3)+"/"+str(m)
            d2 = str(int(d)-2)+"/"+str(m)
            d3 = str(int(d)-1)+"/"+str(m)
            d4 = str(d)+"/"+str(m)
            d5 = str(int(d)+1)+"/"+str(m)
            
            return render(request, 'novo_12.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '5':
            d1 = str(int(d)-4)+"/"+str(m)
            d2 = str(int(d)-3)+"/"+str(m)
            d3 = str(int(d)-2)+"/"+str(m)
            d4 = str(int(d)-1)+"/"+str(m)
            d5 = str(d)+"/"+str(m)
            
            return render(request, 'novo_12.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def novo_13(request):
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
            
            return render(request, 'novo_13.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '2':
            d1 = str(int(d)-1)+"/"+str(m)
            d2 = str(d)+"/"+str(m)
            d3 = str(int(d)+1)+"/"+str(m)
            d4 = str(int(d)+2)+"/"+str(m)
            d5 = str(int(d)+3)+"/"+str(m)
            
            return render(request, 'novo_13.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '3':
            d1 = str(int(d)-2)+"/"+str(m)
            d2 = str(int(d)-1)+"/"+str(m)
            d3 = str(d)+"/"+str(m)
            d4 = str(int(d)+1)+"/"+str(m)
            d5 = str(int(d)+2)+"/"+str(m)
            
            return render(request, 'novo_13.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '4':
            d1 = str(int(d)-3)+"/"+str(m)
            d2 = str(int(d)-2)+"/"+str(m)
            d3 = str(int(d)-1)+"/"+str(m)
            d4 = str(d)+"/"+str(m)
            d5 = str(int(d)+1)+"/"+str(m)
            
            return render(request, 'novo_13.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '5':
            d1 = str(int(d)-4)+"/"+str(m)
            d2 = str(int(d)-3)+"/"+str(m)
            d3 = str(int(d)-2)+"/"+str(m)
            d4 = str(int(d)-1)+"/"+str(m)
            d5 = str(d)+"/"+str(m)
            
            return render(request, 'novo_13.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def novo_21(request):
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
            
            return render(request, 'novo_21.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '2':
            d1 = str(int(d)-1)+"/"+str(m)
            d2 = str(d)+"/"+str(m)
            d3 = str(int(d)+1)+"/"+str(m)
            d4 = str(int(d)+2)+"/"+str(m)
            d5 = str(int(d)+3)+"/"+str(m)
            
            return render(request, 'novo_21.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '3':
            d1 = str(int(d)-2)+"/"+str(m)
            d2 = str(int(d)-1)+"/"+str(m)
            d3 = str(d)+"/"+str(m)
            d4 = str(int(d)+1)+"/"+str(m)
            d5 = str(int(d)+2)+"/"+str(m)
            
            return render(request, 'novo_21.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '4':
            d1 = str(int(d)-3)+"/"+str(m)
            d2 = str(int(d)-2)+"/"+str(m)
            d3 = str(int(d)-1)+"/"+str(m)
            d4 = str(d)+"/"+str(m)
            d5 = str(int(d)+1)+"/"+str(m)
            
            return render(request, 'novo_21.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '5':
            d1 = str(int(d)-4)+"/"+str(m)
            d2 = str(int(d)-3)+"/"+str(m)
            d3 = str(int(d)-2)+"/"+str(m)
            d4 = str(int(d)-1)+"/"+str(m)
            d5 = str(d)+"/"+str(m)
            
            return render(request, 'novo_21.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def novo_22(request):
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
            
            return render(request, 'novo_22.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '2':
            d1 = str(int(d)-1)+"/"+str(m)
            d2 = str(d)+"/"+str(m)
            d3 = str(int(d)+1)+"/"+str(m)
            d4 = str(int(d)+2)+"/"+str(m)
            d5 = str(int(d)+3)+"/"+str(m)
            
            return render(request, 'novo_22.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '3':
            d1 = str(int(d)-2)+"/"+str(m)
            d2 = str(int(d)-1)+"/"+str(m)
            d3 = str(d)+"/"+str(m)
            d4 = str(int(d)+1)+"/"+str(m)
            d5 = str(int(d)+2)+"/"+str(m)
            
            return render(request, 'novo_22.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '4':
            d1 = str(int(d)-3)+"/"+str(m)
            d2 = str(int(d)-2)+"/"+str(m)
            d3 = str(int(d)-1)+"/"+str(m)
            d4 = str(d)+"/"+str(m)
            d5 = str(int(d)+1)+"/"+str(m)
            
            return render(request, 'novo_22.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '5':
            d1 = str(int(d)-4)+"/"+str(m)
            d2 = str(int(d)-3)+"/"+str(m)
            d3 = str(int(d)-2)+"/"+str(m)
            d4 = str(int(d)-1)+"/"+str(m)
            d5 = str(d)+"/"+str(m)
            
            return render(request, 'novo_22.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def novo_23(request):
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
            
            return render(request, 'novo_23.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '2':
            d1 = str(int(d)-1)+"/"+str(m)
            d2 = str(d)+"/"+str(m)
            d3 = str(int(d)+1)+"/"+str(m)
            d4 = str(int(d)+2)+"/"+str(m)
            d5 = str(int(d)+3)+"/"+str(m)
            
            return render(request, 'novo_23.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '3':
            d1 = str(int(d)-2)+"/"+str(m)
            d2 = str(int(d)-1)+"/"+str(m)
            d3 = str(d)+"/"+str(m)
            d4 = str(int(d)+1)+"/"+str(m)
            d5 = str(int(d)+2)+"/"+str(m)
            
            return render(request, 'novo_23.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '4':
            d1 = str(int(d)-3)+"/"+str(m)
            d2 = str(int(d)-2)+"/"+str(m)
            d3 = str(int(d)-1)+"/"+str(m)
            d4 = str(d)+"/"+str(m)
            d5 = str(int(d)+1)+"/"+str(m)
            
            return render(request, 'novo_23.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
        if dia == '5':
            d1 = str(int(d)-4)+"/"+str(m)
            d2 = str(int(d)-3)+"/"+str(m)
            d3 = str(int(d)-2)+"/"+str(m)
            d4 = str(int(d)-1)+"/"+str(m)
            d5 = str(d)+"/"+str(m)
            
            return render(request, 'novo_23.html', {'title':'Novo Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar(request):
    if request.user.is_authenticated():
        pacientes = paciente.objects.all().order_by('nome')
        professores = professor.objects.all().order_by('nome')
        planos = plano.objects.all().order_by('nome')
        agenda_id = request.GET.get('agenda_id')
        agenda_obj = agendamento.objects.filter(id=agenda_id).get()
        dia = agenda_obj.data.strftime('%w')
        d = agenda_obj.data.strftime('%d')
        m = agenda_obj.data.strftime('%m')
        y = agenda_obj.data.strftime('%Y')
        if request.method == 'POST' and request.POST.get('plan') == '2':
            age_id = request.POST.get('age_id')
            age_obj = agendamento.objects.filter(id=age_id).get()
            pac_id = request.POST.get('pac')
            pac = paciente.objects.filter(id=pac_id).get()
            prof_id = request.POST.get('prof')
            prof = professor.objects.filter(id=prof_id).get()
            horario = request.POST.get('hora')
            dia = request.POST.get('dia')
            data_obj = datetime.strptime(''+y+' '+m+' '+dia+' '+horario+'', '%Y %m %d %H:%M')
            age_obj.aluno = pac
            age_obj.prof1 = prof
            age_obj.data = data_obj
            age_obj.save()
            if data_obj.strftime('%w') == '1':
                data = "Segunda-Feira as "+horario+""  
                msg = "Agendamento editado com sucesso."
                return render(request, 'home/home.html', {'title':'Home', 'msg':msg, 'age_obj':age_obj, 'data':data})
            elif data_obj.strftime('%w') == '2':
                data = "Terca-Feira as "+horario+""  
                msg = "Agendamento editado com sucesso."
                return render(request, 'home/home.html', {'title':'Home', 'msg':msg, 'age_obj':age_obj, 'data':data})
            elif data_obj.strftime('%w') == '3':
                data = "Quarta-Feira as "+horario+""
                msg = "Agendamento editado com sucesso."
                return render(request, 'home/home.html', {'title':'Home', 'msg':msg, 'age_obj':age_obj, 'data':data})
            elif data_obj.strftime('%w') == '4':
                data = "Quinta-Feira as "+horario+"" 
                msg = "Agendamento editado com sucesso."
                return render(request, 'home/home.html', {'title':'Home', 'msg':msg, 'age_obj':age_obj, 'data':data})
            elif data_obj.strftime('%w') == '5':
                data = "Sexta-Feira as "+horario+""
                msg = "Agendamento editado com sucesso."
                return render(request, 'home/home.html', {'title':'Home', 'msg':msg, 'age_obj':age_obj, 'data':data})
            msg = "Agendamento editado com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg, 'age_obj':age_obj})
        if dia == '1':
            d1 = str(d)
            d2 = str(int(d)+1)
            d3 = str(int(d)+2)
            d4 = str(int(d)+3)
            d5 = str(int(d)+4)
            
            return render(request, 'editar.html', {'title':'Editar Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5, 'm':m, 'agenda_obj':agenda_obj})
        if dia == '2':
            d1 = str(int(d)-1)
            d2 = str(d)
            d3 = str(int(d)+1)
            d4 = str(int(d)+2)
            d5 = str(int(d)+3)
            
            return render(request, 'editar.html', {'title':'Editar Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5, 'm':m, 'agenda_obj':agenda_obj})
        if dia == '3':
            d1 = str(int(d)-2)
            d2 = str(int(d)-1)
            d3 = str(d)
            d4 = str(int(d)+1)
            d5 = str(int(d)+2)
            
            return render(request, 'editar.html', {'title':'Editar Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5, 'm':m, 'agenda_obj':agenda_obj})
        if dia == '4':
            d1 = str(int(d)-3)
            d2 = str(int(d)-2)
            d3 = str(int(d)-1)
            d4 = str(d)
            d5 = str(int(d)+1)
            
            return render(request, 'editar.html', {'title':'Editar Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5, 'm':m, 'agenda_obj':agenda_obj})
        if dia == '5':
            d1 = str(int(d)-4)
            d2 = str(int(d)-3)
            d3 = str(int(d)-2)
            d4 = str(int(d)-1)
            d5 = str(d)
            
            return render(request, 'editar.html', {'title':'Editar Agendamento', 'pacientes':pacientes, 'professores':professores, 'dia':dia, 'planos':planos, 'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5, 'm':m, 'agenda_obj':agenda_obj})
        return render(request, 'editar.html', {'title':'Editar Agenda'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})