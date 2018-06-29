from django.shortcuts import render
from conta.models import conta
from caixa.models import caixa_geral
from datetime import datetime
from decimal import Decimal
# Create your views here.

def conta1(request):
    if request.user.is_authenticated():
        return render(request, 'conta.html', {'title':'Contas'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})
def nova(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('name') != None:
            name = request.POST.get('name')
            valor = request.POST.get('valor')
            desc = request.POST.get('desc')
            data = request.POST.get('date')
            nava_conta = conta(nome=name, valor=valor, descricao=desc, data_venc=data, estado=1)
            nava_conta.save()
            msg = "Conta agendada com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'nova_conta.html', {'title':'Contas'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})
    return render(request, 'home/erro.html', {'title':'Erro'})

def editar(request):
    if request.user.is_authenticated():
        contas = conta.objects.filter(estado=1).all()
        if request.method == 'POST' and request.POST.get('conta_id') != None:
            conta_id = request.POST.get('conta_id')
            edita_conta = conta.objects.filter(id=conta_id).get()
            return render(request, 'editar_conta.html', {'title':'Editar Conta', 'conta_obj':edita_conta})
        return render(request, 'edita_conta.html', {'title':'Editar Conta', 'contas':contas})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})
    
def salvar(request):
    if request.user.is_authenticated() and request.method == 'POST':
        conta_id = request.POST.get('id')
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        valor = request.POST.get('valor')
        data = request.POST.get('date')
        salva_conta = conta.objects.filter(id=conta_id).get()
        salva_conta.nome = name
        salva_conta.valor = valor
        salva_conta.descricao = desc
        salva_conta.data_venc = data
        salva_conta.save()
        msg = "Conta editada com sucesso."
        return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def pagar(request):
    if request.user.is_authenticated():
        contas = conta.objects.filter(estado=1).all()
        if request.method == 'POST' and request.POST.get('conta_id') != None:
            conta_id = request.POST.get('conta_id')
            paga_conta = conta.objects.filter(id=conta_id).get()
            paga_conta.estado = 2
            paga_conta.save()
            caixa = caixa_geral.objects.latest('id')
            total = caixa.total - paga_conta.valor
            desc = "Pagamento da "+str(paga_conta.nome)+" "+str(paga_conta.data_venc.strftime('%d/%m/%Y'))+" -- R$ "+str(paga_conta.valor)+"."
            novo_caixa = caixa_geral(tipo=2, total=total, desc=desc)
            novo_caixa.save()
            msg = "Conta paga com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'paga_conta.html', {'title':'Pagar Conta', 'contas':contas})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})