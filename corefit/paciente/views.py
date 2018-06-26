from django.shortcuts import render
from .models import paciente
# Create your views here.
def pacient(request):
    return render(request, 'paciente.html', {'title':'Pacientes'})

def novo_pac(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('name') != None :
            nome = request.POST.get('name')
            tel = request.POST.get('tel')
            cel =request.POST.get('cel')
            data_nasc = request.POST.get('data_nasc')
            atv = request.POST.get('ativo')
            queixa = request.POST.get('queixa')
            objetivo = request.POST.get('objetivo')
            try:
                novo_paciente = paciente(nome=nome, telefone=tel, celular=cel, data_nasc=data_nasc, ativo=atv, queixa=queixa, objetivo=objetivo)
                novo_paciente.save()
            except:
                novo_paciente = paciente(nome=nome, telefone=tel, celular=cel, queixa=queixa, objetivo=objetivo)
                novo_paciente.save()
            msg = "Novo paciente cadastrado com sucesso!"
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'novo_pac.html', {'title':'Novo Paciente'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})
    

def busca_pac(request):
    if request.user.is_authenticated():
        pacs = paciente.objects.all().order_by('nome')
        if request.method == 'POST' and request.POST.get('id'):
            id = request.POST.get('id')
            pac = paciente.objects.filter(id=id).get()
            return render(request, 'edita_pac.html', {'title':'Editar Paciente', 'pac':pac})
        return render(request, 'busca_pac.html', {'title':'Buscar Paciente', 'pacs':pacs})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def edita_pac(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            pac_id = request.POST.get('id')
            nome = request.POST.get('name')
            tel = request.POST.get('tel')
            cel =request.POST.get('cel')
            data_nasc = request.POST.get('data_nasc')
            atv = request.POST.get('ativo')
            queixa = request.POST.get('queixa')
            objetivo = request.POST.get('objetivo')
            edit_pac = paciente.objects.filter(id=pac_id).get()
            edit_pac.nome = nome
            edit_pac.telefone = tel
            edit_pac.celular = cel
            edit_pac.data_nasc = data_nasc
            edit_pac.ativo = atv
            edit_pac.queixa = queixa
            edit_pac.objetivo = objetivo
            edit_pac.save()
            msg = "Paciente editado com sucesso!"
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})