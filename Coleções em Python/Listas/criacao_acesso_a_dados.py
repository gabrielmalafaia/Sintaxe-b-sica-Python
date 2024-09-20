# Entender o funcionamento da estrutura de dados lista.

# Criando Listas
# Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto.
# Podemos criar listas utilizando o construtor 'list', a função range
# Colocando valores separados por vírgula dentro de colchetes.
# Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.

# Exemplo 
# Declaração de Listas

frutas = ["laranja", "maçã", "uva"]
print(frutas)
frutas = []

letras = list("python") # Uma string é um objeto iterável, ou seja a variável letras, irá armazenar
# as letras presentes na string [p, y, t, h, o, n]

numeros = list(range(10)) # O range vai gerar um lista de valores de 0 a 9
print(numeros)
carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True] # A lista aceita diversos tipos de dados

# Acesso direto

# A lista é uma sequência, portanto podemos acessar seus dados utilizando índices.
# Contamos o índice de determiada sequência a partir do zero.
# A lista é um objeto based-zero

# Exemplo

frutas = ["laranja", "maçã", "uva", "pera"]

frutas[0] # laranja
frutas[2] # uva

# Índices negativos
# Sequências suportam indexação negativa, a contagem começa em -1.
# Isso irá selecionar o ultimo item da lista

frutas = ["laranja", "maçã", "uva", "pera"]

frutas[-1] # pera
frutas[-3] # maçã

# Listas aninhadas

# Listas podem armazenar todos os tipos de objetos Python.
# Portanto podemos ter listas que armazenam outras listas.
# Com isso podemos criar estruturas bidmensionais (tabelas, matriz)
# E acessar informando os índices de linha e coluna.

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]

]

matriz[0] #[1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"

# Fatiamento

# Além de acessar elementos diretamente, podemos extrair um conjunto de valores de um sequência.
# Para isso basta passar o índice inicial e/ou final para acessar o conjunto.
# Podemos ainda informar quantas posições o cursos deve "pular"no acesso
# Fatiamento de strings é uma técnica utilizada para retornar substring(partes da string original)
# Informando inicio (start), fim (stop) e passo (step): [start: stop[,step]].

lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"] Inicia pelo índice 2
lista[:2] # ["p", "y"] # usa o índice 2 (-1) como ponto de parada
lista[1:3] # ["y", "t"] # Inicia pelo índice 1 e para no índicie 3(-1)
lista[0:3:2] # ["p", "t"] Inicia pelo índice 0 vai até o índice 3(-1) e andamos de 2 em 2 caracteres[step]
lista[::] # ["p", "y", "t", "h", "o", "n"] Retorna a lista completa
lista[::-1] # ["n", "o", "h", "t", "y", "p"] Retorna a lista completa ao inverso [espelhar]

# Iterar listas
# A forma mais comum para percorrer os dados de uma lista é utilizando o comando for.

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# Função enumerate
# Às vezes é necessario saber qual o índice do objeto dentro do laço for.
# Para isso podemos usar a função "enumerate"

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice},{carro}")

# Compreensão de listas

# A compreensão de listas ofere uma sintaxe mais curta quando você deseja:
# Criar uma nova lista com base nos valores de uma lista existente (filtro)
# Ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

# Teste
lista = [range(10)]
print(lista)



