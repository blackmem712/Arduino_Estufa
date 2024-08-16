from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Estufa
from django.contrib import messages
from pyfirmata import Arduino, util
import time

# Configuração do Arduino
PORTA = 'COM3'  # Substitua pela sua porta serial
try:
    BOARD = Arduino(PORTA)
    it = util.Iterator(BOARD)
    it.start()
    SENSOR_UMIDADE_PIN = BOARD.get_pin('a:0:i')  # Pino analógico A0 para umidade
    SENSOR_TEMPERATURA_PIN = BOARD.get_pin('a:1:i')  # Pino analógico A1 para temperatura
    RELE_PIN = BOARD.get_pin('d:2:o')  # Pino digital 2 para o relé
    SENSOR_UMIDADE_PIN.enable_reporting()
    SENSOR_TEMPERATURA_PIN.enable_reporting()
except Exception as e:
    BOARD = None
    print(f"Erro ao conectar na porta {PORTA}: {e}")

def ler_umidade():
    """Função para ler a umidade do solo."""
    if BOARD is None:
        return None
    valor = SENSOR_UMIDADE_PIN.read()
    if valor is not None:
        return int(valor * 100)  # Converte para porcentagem
    return None

def ler_temperatura():
    """Função para ler a temperatura."""
    if BOARD is None:
        return None
    valor = SENSOR_TEMPERATURA_PIN.read()
    if valor is not None:
        volts = valor * 5000  # Converte para milivolts
        temp_celsius = (volts - 500) * 0.1  # Calcular temperatura em Celsius
        return temp_celsius
    return None

def controlar_rele(umidade, temperatura):
    """Função para controlar o relé baseado na umidade e temperatura."""
    if umidade <= 50 and temperatura > 27:
        RELE_PIN.write(1)  # Liga o relé
        return True
    else:
        RELE_PIN.write(0)  # Desliga o relé
        return False

def estufa(request):
    """View principal para exibir a lista de estufas, umidade e temperatura."""
    umidade_atual = ler_umidade()
    temperatura_atual = ler_temperatura()
    
    if umidade_atual is not None and temperatura_atual is not None:
        rele_status = controlar_rele(umidade_atual, temperatura_atual)
    else:
        rele_status = None
    
    estufa_list = Estufa.objects.all()
    return render(request, 'home.html', {
        'estufas': estufa_list,
        'umidade_atual': umidade_atual,
        'temperatura_atual': temperatura_atual,
        'rele_status': rele_status,
    })

def processa_form(request):
    """View para processar o formulário de adição de uma nova estufa."""
    if request.method == "POST":
        nome = request.POST.get('nome')
        setor = request.POST.get('setor')
        descricao = request.POST.get('descricao')

        if nome and setor and descricao:
            estufa = Estufa(nome=nome, setor=setor, descricao=descricao)
            estufa.save()
            messages.success(request, 'Estufa adicionada com sucesso!')
            return redirect('estufa')
        else:
            messages.error(request, 'Todos os campos são obrigatórios.')

    return render(request, 'home.html')
