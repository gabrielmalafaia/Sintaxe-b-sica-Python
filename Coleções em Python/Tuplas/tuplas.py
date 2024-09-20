# Como se fosse a irmã da lista
# Entender o funcionamento da estrutura de dados tupla

# Criando tuplas

# Tuplas são estruturas de daso muito parecidas com as litas, a principal diferença é que tuplas sãp imutáveis
# Enquanto listas são mutáveis
# Podemos criar tuplas através da classe "tuple", ou colocando valores separados por vírgula de parenteses
# sempre terminar com vírgula exceto quando chamar o método

# Exemplo

frutas = ("laranja", "pera", "uva", "maçã")

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

# Acesso direto

# É muito parecido com uma lista

frutas[0] # laranha
frutas[2] # uva
frutas[-1] # maçã
frutas[-3] # pera

# Tuplas Aninhadas

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

matriz[0] # (1, "a", 2)
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # c

# Fatiamento igual a lista

tupla = tuple("python")

print(tupla)

tupla[2:] # ('t', 'h', 'o', 'n')
tupla[:2] # ('p', 'y')
tupla[1:3] #  ('y', 't')
tupla[0:3:2] # ('p', 't')
tupla[::] # ('p', 'y', 't', 'h', 'o', 'n')
tupla[::-1] # ('n', 'o', 'h', 't', 'y', 'p')

# Iterar igual a lista

carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)

# Função enumerade

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")