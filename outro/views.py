from django.shortcuts import render
from caixa.models import caixa_geral
from .models import professor
from django.utils import timezone
from datetime import timedelta
# Create your views here.
def outro(request):
    if request.user.is_authenticated():
        return render(request, 'outro.html', {'title':'Outros'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def prof(request):
    if request.user.is_authenticated():
        return render(request, 'prof/prof.html', {'title':'Profissionais'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def novo_prof(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('nome') != None:
            nome = request.POST.get('nome') 
            tel = request.POST.get('tel') 
            cel = request.POST.get('cel') 
            data_nasc = request.POST.get('data_nasc') 
            novo_prof = professor(nome=nome, telefone=tel, celular=cel, data_nasc=data_nasc)
            novo_prof.save()
            msg = "Novo profissional salvo com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'prof/novo_prof.html', {'title':'Novo Profissional'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar_prof(request):
    if request.user.is_authenticated():
        profs = professor.objects.all().order_by('nome')
        if request.method == 'POST' and request.POST.get('prof_id') != None:
            prof_id = request.POST.get('prof_id')
            prof = professor.objects.filter(id=prof_id).get()
            return render(request, 'prof/editar_prof.html', {'title':'Editar Profissional', 'prof':prof})
        return render(request, 'prof/busca_prof.html', {'title':'Editar Profissional', 'profs':profs})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def salvar(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('prof_id') != None:
            prof_id = request.POST.get('prof_id')
            prof = professor.objects.filter(id=prof_id).get()
            nome = request.POST.get('nome') 
            tel = request.POST.get('tel') 
            cel = request.POST.get('cel') 
            data_nasc1 = request.POST.get('data') 
            if nome != None:
                prof.nome = nome
            if tel != None:
                prof.telefone = tel
            if cel != None:
                prof.celular = cel
            if data_nasc1 == None or data_nasc1 == "":
                prof.data_nasc = prof.data_nasc
            else:
                prof.data_nasc = data_nasc1
            prof.save()
            msg = "Novo profissional editado com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'prof/novo_prof.html', {'title':'Novo Profissional'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def balanco(request):
    if request.user.is_authenticated():
        return render(request, 'balanco.html', {'title':'Balanco'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def anual(request):
    if request.user.is_authenticated():
        return render(request, 'anual.html', {'title':'Balanco Anual'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def trimestral(request):
    if request.user.is_authenticated():
        return render(request, 'trimestral.html', {'title':'Balanco Trimestral'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def mensal(request):
    if request.user.is_authenticated():
        mes = timezone.now().strftime('%m')
        fat = 0
        luc = 0
        cus = 0
        for f in caixa_geral.objects.filter(data__month=mes, tipo=1).all():
            fat = fat + f.total
        for c in caixa_geral.objects.filter(data__month=mes, tipo=2).all():
            cus = cus + c.total
        luc = fat + cus
        return render(request, 'mensal.html', {'title':'Balanco Mensal', 'fat':fat, 'cus':cus, 'luc':luc})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def diario(request):
    if request.user.is_authenticated():
        hoje = timezone.now().strftime('%Y-%m-%d')
        caixas = caixa_geral.objects.filter(data__contains=hoje).all()
        if request.method == 'POST' and request.POST.get('data') != None:
            data1 = request.POST.get('data')
            caixas = caixa_geral.objects.filter(data__icontains=data1)
            return render(request, 'diario.html', {'title':'Extrato', 'caixas':caixas, 'hoje':data1})   
        return render(request, 'diario.html', {'title':'Balanco Diario', 'caixas':caixas, 'hoje':hoje})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

