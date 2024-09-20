# {}.union
# Usado para unir dois conjuntos

set_a = {1, 2}
set_b = {3, 4}

print(set_a.union(set_b)) # 1, 2, 3, 4

# {}.intersection
# Interscção exibe a parte do conjunto que são iguais

set_a = {1, 2, 3}
set_b = {2, 3, 4}

print(set_a.intersection(set_b)) # 2, 3

# {}.difference
# Exibe o que tem de diferente em um conjunto

print(set_a.difference(set_b)) # 1
print(set_b.difference(set_a)) # 4

# {}.symmetric_difference

# É tudo que não está na intersecção

print(set_a.symmetric_difference(set_b)) # 1, 4

# {}.issubset

# Verifica se os objetos de um conjunto pertencem a outro conjunto e devolve um booleano

set_a = {1, 2, 3}
set_b = {4, 1, 2, 5, 6, 3}

print(set_a.issubset(set_b))
print(set_b.issubset(set_a))

# {}.issuperset

# É ao contrário do método acima

print(set_a.issuperset(set_b))
print(set_b.issuperset(set_a))

# {}.isdisjoint
# Um conjunto que não se tocam, demonstra que não tem um valor dentro do outro

set_a = {1, 2, 3, 4, 5}
set_b = {6, 7, 8, 9}
set_c = {1, 0}

print(set_a.isdisjoint(set_b))
print(set_a.isdisjoint(set_c))

# {}.add
# Pode passar um elemento, se ele não existir ele é adicionado

sorteio = {1, 25}

sorteio.add(23)
sorteio.add(42)
sorteio.add(25)

print(sorteio)

# {}.clear
sorteio = {1, 23}
sorteio.clear()

# {}.copy

sorteio = {1, 23}
sorteio.copy()

# {}.discard
# descarta um objeto

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45) # Não retorna erro

# {}.pop
# Remove o índice 0
numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

numeros.pop() # 0

# {}.remove

# É parecido com o discard, mas se eu passar um elemento que não existe ele retorna um erro

numeros.remove(1)

# len - retorna o tamanho do conunto

print(len(numeros))

# In, verifica se um numero está dentro do objeto

print(3 in numeros)
print(10 in numeros)