# Fazendo operações aritméticas usando váriaveis

produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

# O python respeita a prescedência, mas se quiser forçar uma sequencia de prescedência diferente, use ()
x = (10 + 5) * 4
y = (10 / 2) + (25 * 2) - (2 ** 2) # É uma boa prática deixar explicito com paretêses a prescedência
# Mesmo que o python faça isso automaticamente
print(x)
print(y)
