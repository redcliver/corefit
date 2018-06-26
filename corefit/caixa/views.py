from django.shortcuts import render
from .models import caixa_geral
from decimal import Decimal
# Create your views here.
def caixa(request):
    if request.user.is_authenticated():
        try:
            caixa = caixa_geral.objects.latest('id')
        except:
            caixa = caixa_geral(tipo=1, total=0, desc="Abertura do caixa")
            caixa.save()
        return render(request, 'caixa.html', {'title':'Caixa', 'caixa':caixa})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def entrada(request):
    if request.user.is_authenticated():
        caixa = caixa_geral.objects.latest('id')
        if request.method == 'POST' and request.POST.get('entrada') != None:
            valor_entrada = request.POST.get('entrada')
            mot = request.POST.get('motivo')
            total = caixa.total + Decimal(valor_entrada)
            novo_caixa  = caixa_geral(tipo=1, total=total, desc=""+str(mot)+" -- R$ "+str(valor_entrada)+".")
            novo_caixa.save()
            msg = "Entrada registrada com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'entrada.html', {'title':'Entradas', 'caixa':caixa})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def retirada(request):
    if request.user.is_authenticated():
        caixa = caixa_geral.objects.latest('id')
        if request.method == 'POST' and request.POST.get('retirada') != None:
            valor_retirada = request.POST.get('retirada')
            mot = request.POST.get('motivo')
            total = caixa.total - Decimal(valor_retirada)
            novo_caixa  = caixa_geral(tipo=2, total=total, desc=""+str(mot)+" -- R$ "+str(valor_retirada)+".")
            novo_caixa.save()
            msg = "Retirada registrada com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'retirada.html', {'title':'Retirada', 'caixa':caixa})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def fechar(request):
    if request.user.is_authenticated():
        caixa = caixa_geral.objects.latest('id')
        if request.method == 'POST' and request.POST.get('fechamento') != None:
            valor_fechamento = request.POST.get('fechamento')
            total = caixa.total - Decimal(valor_fechamento)
            novo_caixa  = caixa_geral(tipo=2, total=total, desc="Fechamento de caixa -- R$ "+str(valor_fechamento)+".")
            novo_caixa.save()
            msg = "Caixa fechado com sucesso."
            return render(request, 'home/home.html', {'title':'Home', 'msg':msg})
        return render(request, 'fechar.html', {'title':'Fechar', 'caixa':caixa})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})