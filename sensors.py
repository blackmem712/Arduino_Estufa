from pyfirmata import Arduino, util
import time
import requests

URL = 'http://127.0.0.1:8000/estufa/'
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
    print(f"Conectado ao Arduino na porta {PORTA}")
except Exception as e:
    BOARD = None
    print(f"Erro ao conectar na porta {PORTA}: {e}")

def ler_umidade():
    if BOARD is None:
        print("Erro: BOARD é None. Verifique a conexão com o Arduino.")
        return None
    valor = SENSOR_UMIDADE_PIN.read()
    if valor is not None:
        umidade = int(valor * 100)
        print(f"Umidade lida: {umidade}%")
        return umidade
    print("Erro ao ler a umidade.")
    return None

def ler_temperatura():
    if BOARD is None:
        print("Erro: BOARD é None. Verifique a conexão com o Arduino.")
        return None
    valor = SENSOR_TEMPERATURA_PIN.read()
    if valor is not None:
        volts = valor * 5000
        temp_celsius = (volts - 500) * 0.1
        print(f"Temperatura lida: {temp_celsius:.1f}°C")
        return temp_celsius
    print("Erro ao ler a temperatura.")
    return None

def controlar_rele(umidade, temperatura):
    if umidade < 50 and temperatura > 10:
        RELE_PIN.write(1)
        print("Relé ligado.")
        return True
    else:
        RELE_PIN.write(0)
        print("Relé desligado.")
        return False
    
def enviar_dados_para_servidor(umidade, temperatura):
    url = 'http://127.0.0.1:8000/estufa/'  # URL do endpoint no servidor Django
    try:
        dados = {
            'umidade': umidade,
            'temperatura': temperatura
        }
        response = requests.post(URL, data=dados)
        
        if response.status_code == 200:
            print("Dados enviados com sucesso.")
        else:
            print(f"Falha ao enviar dados: {response.status_code}")
            print(f"Resposta do servidor: {response.text}")
    except Exception as e:
        print(f"Erro ao enviar os dados: {e}")

def loop_principal():
    while True:
        umidade = ler_umidade()
        temperatura = ler_temperatura()
        if umidade is not None and temperatura is not None:
            controlar_rele(umidade, temperatura)
            enviar_dados_para_servidor(umidade, temperatura)
        time.sleep(5)  # Aguarda 10 segundos antes de tentar novamente
          
      

if __name__ == "__main__":
    loop_principal()