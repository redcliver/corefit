from django.shortcuts import render
from .models import teste

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        return render(request, 'home/home.html', {'title':'Home'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})