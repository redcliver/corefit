from django.shortcuts import render
import ctypes
import hello
# Create your views here.
def presenca(request):
    if request.user.is_authenticated():
        dll = hello
        return render(request, 'presenca.html', {'title':'Presenca', 'dll':dll})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})