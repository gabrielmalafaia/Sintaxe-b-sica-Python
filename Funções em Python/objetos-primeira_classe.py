# Eem python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos de primeira classe.
# Com isso podemos atribuir funções a variáveis, passá-las como parâmetros para funções, usá=las
# como valores em estruturas de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função(closures)

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def exibir_resultado(a, b, funcao): # Essa função recebe 3 parâmetro a, b, funcao(é só um nome)
    resultado = funcao(a, b) 
    print(f"O resultado da operação é igual a {resultado}")

exibir_resultado(10, 10, somar)# passo os parâmetros e passo só a referencia da função somar, não a executo
# executando ela seria somar(), passo ela sem os "()"

exibir_resultado(10, 10, subtrair)
exibir_resultado(10, 10, multiplicar)

op = somar

print(op(1,23))