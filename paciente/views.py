from django.shortcuts import render
from .models import paciente
from outro.models import professor
from plano.models import plano
from django.utils.dateparse import parse_date
# Create your views here.
def pacient(request):
    return render(request, 'paciente.html', {'title':'Pacientes'})

def novo_pac(request):
    if request.user.is_authenticated():
        professores = professor.objects.all().order_by('nome')
        planos = plano.objects.all().order_by('nome')
        if request.method == 'POST' and request.POST.get('name') != None :
            nome = request.POST.get('name')
            tel = request.POST.get('tel')
            cel =request.POST.get('cel')
            data_nasc = request.POST.get('data_nasc')
            atv = request.POST.get('ativo')
            periodo = request.POST.get('periodo')
            data_v = request.POST.get('data_v')
            prof = request.POST.get('profissional')
            queixa = request.POST.get('queixa')
            objetivo = request.POST.get('objetivo')
            try:
                profissional = professor.objects.filter(id=prof).get()
            except:
                profissional = None

            try:
                peri = plano.objects.filter(id=periodo).get()
            except:
                peri = None

            try:
                novo_paciente = paciente(nome=nome, telefone=tel, celular=cel, data_nasc=data_nasc, ativo=atv, data_venc=data_v, prof1=profissional, plan1=peri, queixa=queixa, objetivo=objetivo)
                novo_paciente.save()
            except:
                novo_paciente = paciente(nome=nome, telefone=tel, celular=cel, ativo=atv, data_venc=data_v, prof1=profissional, plan1=peri, queixa=queixa, objetivo=objetivo)
                novo_paciente.save()
            msg = "Novo paciente cadastrado com sucesso!"
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'novo_pac.html', {'title':'Novo Paciente', 'professores':professores, 'planos':planos})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})
    

def busca_pac(request):
    if request.user.is_authenticated():
        pacs = paciente.objects.all().order_by('nome')
        if request.method == 'POST' and request.POST.get('pac_id'):
            pac_id = request.POST.get('pac_id')
            pac_obj = paciente.objects.filter(id=pac_id).get()
            professores = professor.objects.all().order_by('nome')
            return render(request, 'edita_pac.html', {'title':'Editar Paciente', 'pac_obj':pac_obj, 'professores':professores})
        return render(request, 'busca_pac.html', {'title':'Buscar Paciente', 'pacs':pacs})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def edita_pac(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            pac_id = request.POST.get('id')
            edit_pac = paciente.objects.filter(id=pac_id).get()
            if request.POST.get('profissional') != None:
                prof2 = request.POST.get('profissional')
                prof_novo = professor.objects.filter(id=prof2).get()
                edit_pac.prof1 = prof_novo
                edit_pac.save()
            else:
                prof_novo = edit_pac.prof1

            if request.POST.get('data_v') != None and request.POST.get('data_v') != '':
                data_v = request.POST.get('data_v')
                edit_pac.data_venc = parse_date(data_v)
                edit_pac.save()
            

            if request.POST.get('name') != edit_pac.nome or request.POST.get('name') is not None:
                edit_pac.nome = request.POST.get('name')
                edit_pac.save()
            if request.POST.get('tel') != edit_pac.telefone or request.POST.get('tel') is not None:
                edit_pac.telefone = request.POST.get('tel')
                edit_pac.save()
            if request.POST.get('cel') != edit_pac.telefone or request.POST.get('cel') is not None:
                edit_pac.celular = request.POST.get('cel')
                edit_pac.save()
            if request.POST.get('ativo') != edit_pac.ativo or request.POST.get('ativo') is not None:
                edit_pac.ativo = request.POST.get('ativo')
                edit_pac.save()
            if request.POST.get('queixa') != edit_pac.queixa or request.POST.get('queixa') != '':
                quei = request.POST.get('queixa')
                edit_pac.queixa = quei
                edit_pac.save()
            if request.POST.get('obj') != edit_pac.objetivo or request.POST.get('obj') != '':
                obj = request.POST.get('obj')
                edit_pac.objetivo = obj
                edit_pac.save()
            if request.POST.get('data_nasc') != edit_pac.data_nasc and request.POST.get('data_nasc') != '':
                data = request.POST.get('data_nasc')
                edit_pac.data_nasc = parse_date(data)
                edit_pac.save()
            msg = "Paciente editado com sucesso!"
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})