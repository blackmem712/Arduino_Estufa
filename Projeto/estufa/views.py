from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Estufa
from django.contrib import messages
from pyfirmata import Arduino,util
import time


PORTA = 'COM3'  # Substitua pelo seu porto serial
try:
    BOARD = Arduino(PORTA)
    it = util.Iterator(BOARD)
    it.start()
    SENSOR_PIN = BOARD.get_pin('a:0:i')  # Definindo o pino analógico A0
    SENSOR_PIN.enable_reporting()
except Exception as e:
    BOARD = None
    print(f"Erro ao conectar na porta {PORTA}: {e}")

def ler_umidade():
    if BOARD is None:
        return None
    valor = SENSOR_PIN.read()
    if valor is not None:
        return int(valor * 100)  # Converte para porcentagem
    return None

def estufa(request):
  umidade_atual = ler_umidade()
  estufa_list = Estufa.objects.all()
  return render(request, 'home.html',{'estufas': estufa_list,'umidade_atual': umidade_atual,})


def processa_form(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        setor = request.POST.get('setor')
        descricao = request.POST.get('descricao')

        if nome and setor and descricao:
            estufa = Estufa(nome=nome, setor=setor, descricao=descricao)
            estufa.save()
            messages.success(request, 'Estufa adicionada com sucesso!')
            return redirect('estufa')  # Assumindo que 'estufa' é o nome do padrão de URL para a view estufa
        else:
            messages.error(request, 'Todos os campos são obrigatórios.')

    return render(request, 'home.html')