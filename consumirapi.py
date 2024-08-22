import requests

API_KEY ="58a963650ffd1e7ea4fef3e9ff6862e3"
cidade = "Ji-paraná"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requesicao = requests.get(link)
requesicao_dic = requesicao.json()
descricao = requesicao_dic['weather']

print(requesicao_dic)
