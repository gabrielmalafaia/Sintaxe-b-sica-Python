# Métodos da classe lis

# Método [].append
# Quando quero adicionar objetos a minha lista

lista = []

lista.append(1)
lista.append("Python")
lista.append([40,30,20])

print(lista)

# Método [].clear
# Quando eu quero limpar a minha losta

lista.clear()
print(lista)

# Método [].copy
# A lista é um objeto mutável, se eu usar a lista em uma função e alterar algo nela, a lista original 
# sera alterada também para evitar isso, você usa o copy, você copia os objetos que está em uma lista
# e armazina em uma outra lista

lista = [1, "Python", [40, 30, 20]]
l2 = lista.copy()

l2[0] = 2
print(id(l2), id(lista)) # Demonstra que são dois objetos diferentes, mesmo fazendo uma cópia
print(l2)
print(lista)

# Método [].count
# Ele é usado para contar quantas vezes determinado objeto aparece dentro da sua lista

cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1

# Método [].extend
# Parecido com o método append(que pode só adionar objetos de 1 em 1)
# Nesse método eu consigo juntar objetos de uma lista em outra lista

linguagens = ["python", "js", "c"]
print(linguagens) # ["python", "js", "c"]

linguagens.extend(["java", "c#"])
print(linguagens) # ["python", "js", "c", "java", "c#"]

# Método [].index
# É um metódo que mostra em qual índice está determinado valor considerando a primeira ocorrência dele
# Exemplo

print(linguagens.index("c")) # 2

# Método [].pop

# A lista funciona como uma pilha de pratos, vamos supor que você vai adicionando pratos em um local vazio
# Coloca o primeiro, segundo, terceiro até chegar no último
# Se alguém for lá pegar um prato, ele não vai pegar o primeiro e sim o último
# A lista tem esse mesmo comportamento, quando usamos o appen(), extedn(), ele adiciona objetos ao final da lista
# E o método pop quando é chamado ele sempre vai tirar o último elemento da lista quando você não especifica
# Quando você específica o ínidici que quer remover ele remove o número que foi designado

# Exemplo

linguagens.pop() # c#
linguagens.pop() # java
linguagens.pop() # c
linguagens.pop(0) # python

print(linguagens)

# Método [].remove
# É outro método que você pode remover elementos de uma lista, diferente do pop, que você índica o índice
# Aqui você cita o objeto em si
# Se tiver mais de uma ocorrência de um objeto, ele irá remover a primeira ocorrência que aparece

# Exemplo

linguagens = ["python", "js", "c", "java", "c#"]

linguagens.remove("c")
print(linguagens) # ["python", "js", "java", "c#"]

# Método [].reverse

# Em fatiamento aprendemos a espelhar uma lista

linguagens = ["python", "js", "c", "java", "c#"]
print(linguagens[::-1])

# Mas existe um método para isso que é o reverse()
# A diferença é que o reverse altera a lista deixando ela ao contrário
# O fatiamento só exibe ao contrário e não altera a lista

linguagens.reverse()
print(linguagens)

# Método [].sort
# É um método que é usado para ordenar a sua lista

linguagens = ["python", "js", "c", "java", "c#"]
linguagens.sort() # Ele ordenou em ordem alfabética (A a Z)
print(linguagens)

# Dentro do sort() eu posso passar alguns argumentos que são o (reverse, key)
linguagens = ["python", "js", "c", "java", "c#"]
linguagens.sort(reverse=True) # Ele ordena em ordem alfabética mas de traz pra frente (Z a A)
print(linguagens)


# Por padrão o sort vai ordenar as string em ordem alfabética, vamos supor que eu quero ordenar 
# Por tamanho da palavra e colocar por ordem crescente, do que tem menos palavras ao que tem mais
# Nesse caso eu tenho que passa um função, no caso uma função anonima (lamba)
# Nessa função para cada item ele vai executar um código
# O "x" na função vai representar cada objeto da lista
# E o "len" ele retorna o tamanho de uma string, quantos caracteres ela tem
# E por padrão o sort ordena por ordem crescente

# Exemplo

linguagens = ["python", "js", "c", "java", "c#"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)

# Aqui eu faço a mesma coisa, mas retorno a lista ao inverso, do maior para o menor

linguagens = ["python", "js", "c", "java", "c#"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

# Len
# Usado para ver tamanhos de objetos, logo acima usamos ele pra ver tamanhos de string
# Neste exemplo vamos utilizar pra ver o tamanho da nossa lista

linguagens = ["python", "js", "c", "java", "c#"]
len(linguagens) # 5

# .[] sorted
# Uma função que já está inclusa na linguagem, como a função acima
# Tem a mesma função do sort, a diferença que o sort é um método, e o sorted é uma função

sorted(linguagens, key=lambda x: len(x)) # ['c', 'js', 'c#', 'java', 'python']
sorted(linguagens, key=lambda x: len(x), reverse=True) # ['python', 'java', 'js', 'c#', 'c']
sorted(linguagens) # ['c', 'c#', 'java', 'js', 'python']
sorted(linguagens, reverse=True) # ['python', 'js', 'java', 'c#', 'c']




