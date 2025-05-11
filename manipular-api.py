import requests

"""
# Antes verificar de o pip está instalado
    -> pip --version (Se aparecer a versão do pip, está tudo certo. Caso contrário, você precisará instalar o pip primeiro.)

# Instale o módulo requests
    -> pip install requests (ou python -m pip install requests)

# Verifique se foi instalado corretamente
    -> pip show requests (verificar se o pacote foi realmente instalado)

"""

url = "https://randomuser.me/api"

# Fazendo a requisição GET
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    user = data['results'][0]
    name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
    email = user['email']
    country = user['location']['country']

    print(f"Nome: {name}")
    print(f"Email: {email}")
    print(f"País: {country}")
else:
    print(f"Erro de chamada à API: {response.status_code}")