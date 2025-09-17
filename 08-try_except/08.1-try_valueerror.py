# Exemplo de tratamento de exceção ValueError
try:
    numero = int(input("Digite um número inteiro: "))
# 
except ValueError:
    print("Erro: você digitou um valor inválido!")

# Exemplo de captura da exceção em uma variável
try:
    # código que pode causar um ValueError
    numero = int(input("Digite um número inteiro: ")) # Pode causar ValueError
except ValueError as ve:
    print(f"Erro: {ve}")
    # Aqui, "ve" contém a exceção lançada.