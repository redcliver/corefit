from django.shortcuts import render
import ctypes
# Create your views here.
def presenca(request):
    if request.user.is_authenticated():
        dll = ctypes.cdll.LoadLibrary('./SynoAPIEx.so')
        dll.WINAPI.PSGetImage
        return render(request, 'presenca.html', {'title':'Presenca', 'dll':dll})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})