# importar biblioteca
import requests

cnpj ='59298690000150'
url = f'https://api.opencnpj.org/{cnpj}'
res = requests.get(url)

dados = res.json()

print(f'cnpj: {dados["cnpj"]}')
print('Razão Social: ', dados["razao_social"])
print(f'Nome fantasia: {dados["nome_fantasia"]}')
print(f'Situação cadastral: {dados["situacao_cadastral"]}')