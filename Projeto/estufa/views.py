from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Estufa, SensorData
from django.contrib import messages
from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def estufa(request):
    if request.method == "POST":
        umidade = request.POST.get('umidade')
        temperatura = request.POST.get('temperatura')

        if umidade is not None and temperatura is not None:
            print(f"Umidade recebida: {umidade}%")
            print(f"Temperatura recebida: {temperatura}°C")

            umidade = int(float(umidade))
            temperatura = int(float(temperatura))

            # Aqui você pode processar os dados ou salvá-los no banco de dados

            SensorData.objects.create(umidade=umidade, temperatura=temperatura)

           

            # Renderizar a página com os novos dados
            estufa_list = Estufa.objects.all()
            return render(request, 'home.html', {
                'estufas': estufa_list,

                
                'umidade_atual': umidade,
                'temperatura_atual': temperatura,
            })

        return JsonResponse({'status': 'error', 'message': 'Dados incompletos.'}, status=400)

    # GET: Renderizar a página normalmente
    estufa_list = Estufa.objects.all()
    return render(request, 'home.html', {
        'estufas': estufa_list,
        'umidade_atual': None,
        'temperatura_atual': None,
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

def get_latest_data(request):
    # Obtenha os dados mais recentes do banco de dados
    latest_data = SensorData.objects.latest('timestamp')

    umidade = int(latest_data.umidade) if latest_data.umidade.is_integer() else float(latest_data.umidade)
    temperatura = int(latest_data.temperatura) if latest_data.temperatura.is_integer() else float(latest_data.temperatura)
    
    data = {
        'umidade': umidade,
        'temperatura': temperatura,
        'timestamp': latest_data.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    }
    # Renderize o template e passe os dados como contexto
    return  JsonResponse(data)

def dashboard(request):
     return render(request, 'dashboard.html')