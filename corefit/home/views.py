from django.shortcuts import render
from .models import teste

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get(name)
        img = request.POST.get(img)

    return render(request, 'index.html', {'content':'Funcionando'})