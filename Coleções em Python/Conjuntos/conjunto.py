# Entender o funcionamento da estrutura de dados set

# Criando sets
# Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos
# Ou eliminar itens duplicados de um iterável

set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {b, a, c, x, i}

set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}

# Um conjunto pode também ser declarado com {}

linguagem = {"python", "java", "python"}
print(linguagem)

# Acessando dados
# Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar seus valores 
# É necessário converter o conjunto para lista.


linguagem = list(linguagem)
print(linguagem[0])

# Iterar conjuntos
# A forma mais comum para percorrer os dados de um conjunto é utilizando o comando for.

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

# Função enumerate
# Às vezes é necessário saber qual o índice do objeto dentro do laço for.
# Para isso podemos usar a função enumerate.

for carro, indice in enumerate(carros):
    print(f"{indice}:{carro}")
