# API de consulta de CEP, usando requests
import requests

# Solicita o CEP ao usuário
cep = input("Digite seu cep: ")
via_cep = f"https://viacep.com.br/ws/{cep}/json/" # url da API de consulta de CEP
requisicao = requests.get(via_cep) # faz a requisição

print(requisicao) # Esse imprime o status de conexao

# Mostra o conteúdo da requisição em JSON
print(f"CEP: {requisicao.json()['cep']}") 
print(f"Rua: {requisicao.json()['logradouro']}")
print(f"Bairro: {requisicao.json()['bairro']}")
print(f"Cidade: {requisicao.json()['localidade']}")
print(f"Estado: {requisicao.json()['estado']}")








# cep = input("Digite seu CEP: ")

# via_cep = f'https://viacep.com.br/ws/{cep}/json/'
# requisicao = requests.get(via_cep)
# data = requisicao.json()

# print(f"CEP: {data['cep']}")
# print(f"Rua: {data['logradouro']}")
# print(f"Bairro: {data['bairro']}")
# print(f"Cidade: {data['localidade']}")
# print(f"Estado: {data['estado']}")

