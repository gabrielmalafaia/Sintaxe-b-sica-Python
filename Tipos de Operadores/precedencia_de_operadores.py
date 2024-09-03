# Na matemática existe um regra que indica quais operações
# devem ser executadas primeiro. Isso é útil pois ao analisar
# uma expressão, a depender da ordem das operações o valor pode ser diferente
# X= 10 - 5 * 2
# X é igual a 10 ou a 0 ?

# A definição indica a seguinte ordem como a correta:

# Parêntesis
# Expoêntes
# Multiplicações e divisões (da esquerda para a direita)
# Somas e subtrações (da esquerda para a direita)

print(10 - 5 * 2)
print((10 - 5) * 2)
print(10 ** 2 * 2)
print(10 ** (2 * 2))
print(10 / 2 * 4)
