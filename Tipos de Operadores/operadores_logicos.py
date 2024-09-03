# Vamos aprender sobre operadores lógicos e como utilizar eles no nosso código
# São operadores utilizados em conjunto com os operadores de comparação para montar uma expressão lógica
# Quando um operador de comparação é utilizado o resultado retornado é um booleano

saldo = 1000
saque = 200
limite = 100
conta_especial = True

print(saldo >= saque)
print(saque <= limite)

print(saldo >= saque and saque <= limite) # operador and(E) ambas as partes sendo verdadeira retorna true se não retorna false
print(saldo >= saque or saque <= limite) # operador or(OU) apenas um valor precisa ser verdadeiro pra retornar true

# Operador de negação
print(not 1000 > 1500) # 1000 > 1500 = false(usando o not retorna um not false ou seja true)

contatos_emergencia = [] # uma lista vazia = false

print(not contatos_emergencia) # retorna um true por que uma lista vazia = false - retorna um falso negativo = true

print(not "saque 1500") # uma string preenchida é = true sendo assim um falso true retorna false

print(not "") # uma string vazia = false sendo assim um not false é igual a true

# parenteses delimita a prescedência igual as operações aritiméticas

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

print( (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) )

saldo_suficiente = (saldo >= saque and saque <= limite) # verifica se tem saldo suficiente na conta
conta_especial_com_saldo = (conta_especial and saldo >= saque)# verifica se tem saldo suficiente na conta especial

exp = saldo_suficiente or conta_especial_com_saldo

print(exp)


