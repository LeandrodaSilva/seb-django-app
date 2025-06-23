import requests
from django.shortcuts import render
from django.contrib import messages

def index(request):
    ufs = [
        'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
        'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE',
        'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP',
        'SE', 'TO'
    ]
    
    resultados = []
    
    if request.method == 'POST':
        estado = request.POST.get('uf', '').upper()
        cidade = request.POST.get('cidade', '').strip()
        logradouro = request.POST.get('logradouro', '').strip()
        
        if estado and cidade and logradouro:
            try:
                url = f'https://viacep.com.br/ws/{estado}/{cidade}/{logradouro}/json/'
                response = requests.get(url)
                response.raise_for_status()
                resultados = response.json()
                
                if not resultados:
                    messages.info(request, 'Nenhum resultado encontrado para os critérios de busca.')
                
            except requests.exceptions.RequestException as e:
                messages.error(request, f'Erro ao acessar a API de CEP: {str(e)}')
            except ValueError:
                messages.error(request, 'Resposta inválida da API de CEP')
            
            return render(request, 'index.html', {
                'titulo': 'Resultados da Busca',
                'ufs': ufs,
                'selected_uf': estado,
                'cidade': cidade,
                'logradouro': logradouro,
                'resultados': resultados
            })
    
    return render(request, 'index.html', {
        'titulo': 'Formulário',
        'ufs': ufs,
        'selected_uf': request.POST.get('uf', ''),
        'cidade': request.POST.get('cidade', ''),
        'logradouro': request.POST.get('logradouro', ''),
        'resultados': resultados
    })