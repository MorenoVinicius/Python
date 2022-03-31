import requests # Importando biblioteca

API_KEY = "6e401fdf2b11f18db16cd6c71a777534" # Minha chave da API
cidade = input('Digite o nome da cidade : ' ) # Input para pesquisar a temperatura na cidade
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br" #Link da API

req = requests.get(link)

req_dic= req.json() # Codigo que passa informações .

descricao = req_dic['weather'][0]['description'] # Filtrando informações desejadas

temperatura = req_dic['main']['temp']-273.15 # Filtrando e convertendo Kelvin para graus Celsius.

print(descricao,f"{temperatura: .2f}ºC")
