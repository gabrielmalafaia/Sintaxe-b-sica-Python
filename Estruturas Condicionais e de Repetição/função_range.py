# Função range
# Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir
# de um ínicio(inclusivo) para um fim (exclusivo). Se usarmos range(i,j) será produzido:
# i, i+1, i+2, i+3, ..., j-1
# Ela recebe 3 argumentos: stop(obrigatório), start(opcional) e step(opcional)

for numero in range(0, 51, 5):
    print(numero, end=" ")