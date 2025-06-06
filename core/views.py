# core/views.py

from django.shortcuts import render
from django.http import JsonResponse
import json # Embora JsonResponse já cuide da serialização, é bom para contexto

# Dados fictícios de previsão do tempo
WEATHER_DATA = {
    'natal': {'temperatura': '28°C', 'condicao': 'Ensolarado', 'umidade': '70%'},
    'rio de janeiro': {'temperatura': '32°C', 'condicao': 'Céu limpo', 'umidade': '80%'},
    'sao paulo': {'temperatura': '22°C', 'condicao': 'Parcialmente nublado', 'umidade': '65%'},
    'curitiba': {'temperatura': '18°C', 'condicao': 'Chuvoso', 'umidade': '90%'},
    'salvador': {'temperatura': '29°C', 'condicao': 'Nublado com pancadas', 'umidade': '75%'},
    'belo horizonte': {'temperatura': '25°C', 'condicao': 'Ensolarado com nuvens', 'umidade': '60%'},
    'porto alegre': {'temperatura': '20°C', 'condicao': 'Ventoso', 'umidade': '72%'},
    'fortaleza': {'temperatura': '30°C', 'condicao': 'Quente e úmido', 'umidade': '85%'},
    'recife': {'temperatura': '29°C', 'condicao': 'Poucas nuvens', 'umidade': '78%'},
    'manaus': {'temperatura': '31°C', 'condicao': 'Trovoada', 'umidade': '92%'},
}

def index(request):
    """Renderiza a página principal do aplicativo de previsão do tempo."""
    return render(request, 'index.html')

def get_weather(request):
    """
    Recebe o nome da cidade via GET e retorna a previsão como JSON.
    """
    city_name = request.GET.get('city', '').lower().strip() # Pega a cidade, padroniza para minúsculas e remove espaços

    if not city_name:
        return JsonResponse({'error': 'Por favor, digite o nome de uma cidade.'}, status=400) # Bad Request

    weather_info = WEATHER_DATA.get(city_name)

    if weather_info:
        # Prepara a resposta com os dados da previsão
        response_data = {
            'city': city_name.title(), # Capitaliza para exibição
            'temperatura': weather_info['temperatura'],
            'condicao': weather_info['condicao'],
            'umidade': weather_info['umidade'],
            'message': 'Previsão do tempo obtida com sucesso!'
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': f'Previsão não encontrada para {city_name.title()}. Tente outra cidade.'}, status=404) # Not Found