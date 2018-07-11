from django.shortcuts import render
from .models import plano


# Create your views here.
def plano1(request):
    if request.user.is_authenticated():
        return render(request, 'plano.html', {'title':'Planos'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def novo(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('name') != None:
            name = request.POST.get('name')
            valor = request.POST.get('valor')
            peri = request.POST.get('periodo')
            novo_plan = plano(nome=name, valor=valor, periodo=peri)
            novo_plan.save()
            msg = "Novo plano salvo com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'novo_plano.html', {'title':'Novo Plano'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar(request):
    if request.user.is_authenticated():
        planos = plano.objects.all().order_by('nome')
        if request.method == 'POST' and request.POST.get('plano_id') != None:
            plano_id = request.POST.get('plano_id')
            plan = plano.objects.filter(id=plano_id).get()
            return render(request, 'editar_plano.html', {'title':'Editar', 'plan':plan})
        return render(request, 'busca_plano.html', {'title':'Editar', 'planos':planos})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def salvar(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('plano_id') != None:
            plano_id = request.POST.get('plano_id')
            plan = plano.objects.filter(id=plano_id).get()

            plano_nome = request.POST.get('nome')
            plano_periodo = request.POST.get('periodo')
            plano_valor = request.POST.get('valor')

            try:
                plan.nome = plano_nome
            except:
                plan.nome = plan.nome

            if request.POST.get('periodo') != None:
                plan.periodo = plano_periodo
            else:
                plan.periodo = plan.periodo

            try:
                plan.valor =  plano_valor
            except:
                plan.valor =  plan.valor
            plan.save()

            msg = "Plano editado com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'busca_plano.html', {'title':'Editar', 'planos':planos})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})