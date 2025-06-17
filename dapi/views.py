from django.shortcuts import render


# Create your views here.

def index(request):
    cep = request.GET.get('cep', '')
    return render(request, 'index.html', {
        'titulo': 'Formulário',
        'cep': cep,
    })