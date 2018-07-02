from django.shortcuts import render

# Create your views here.
def presenca(request):
    if request.method == 'POST':
        name = request.POST.get(name)
        img = request.POST.get(img)

    return render(request, 'presenca.html', {'title':'Presenca'})