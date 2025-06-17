from django.shortcuts import render


# Create your views here.

def index(request):
    uf = request.GET.get('uf', '')
    cidade = request.GET.get('cidade', '')
    logradouro = request.GET.get('logradouro', '')
    return render(request, 'index.html', {
        'titulo': 'Formulário',
        'selected_uf': uf,
        'cidade': cidade,
        'logradouro': logradouro,
        'ufs': [
            'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
            'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE',
            'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP',
            'SE', 'TO'
        ]
    })