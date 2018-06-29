from django.shortcuts import render
from django.utils.timezone import datetime
# Create your views here.
def agenda1(request):
    if request.user.is_authenticated():
        hoje = datetime.today().strftime('%A, %d de %B de %Y')
        dia_sem = datetime.today().strftime('%A, %d de %B de %Y')
        return render(request, 'agenda.html', {'title':'Agenda', 'hoje':hoje})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})