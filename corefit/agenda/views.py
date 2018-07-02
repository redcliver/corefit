from django.shortcuts import render
from django.utils.timezone import datetime
# Create your views here.
def agenda1(request):
    if request.user.is_authenticated():
        hoje = datetime.today().strftime('%d de %B de %Y')
        dia_sem = datetime.today().strftime('%A, %d de %B de %Y')
        sem = datetime.today().strftime('%a')
        if sem == 'Mon':
            dia = 1
        elif sem == 'Tue':
            dia = 2
        elif sem == 'Wed':
            dia = 3
        elif sem == 'Thu':
            dia = 4
        elif sem == 'Fri':
            dia = 5
        return render(request, 'agenda.html', {'title':'Agenda', 'hoje':hoje, 'dia':dia})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})