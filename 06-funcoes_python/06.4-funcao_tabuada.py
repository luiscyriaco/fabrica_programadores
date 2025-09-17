# Função que exibe a tabuada de um número

def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
        
# Função para imprimir uma linha separadora
def line():
    print('-' * 15)

# Exibe as tabuadas de 1 a 10
print('Tabuadas 1 ao 10')
line()
tabuada(1)
line()
tabuada(2)
line()
tabuada(3)
line()
tabuada(4)
line()
tabuada(5)
line()
tabuada(6)
line()
tabuada(7)
line()
tabuada(8)
line()
tabuada(9)
line()
tabuada(10)
line()
