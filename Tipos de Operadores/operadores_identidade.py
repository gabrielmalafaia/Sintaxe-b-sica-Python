# Operadores de Identidade são operadores utilizados para comparar se os dois objetos testados ocupam
# a mesma posição na memória.

# EXEMPLO 1

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)

# EXEMPLO 2

saldo, limite = 1000, 500

print(saldo is limite)
print(saldo is not limite)