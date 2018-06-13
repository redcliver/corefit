from django.shortcuts import render

# Create your views here.
def paciente(request):
    if request.method == 'POST':
        name = request.POST.get(name)
        img = request.POST.get(img)

    return render(request, 'paciente.html', {'title':'Pacientes'})