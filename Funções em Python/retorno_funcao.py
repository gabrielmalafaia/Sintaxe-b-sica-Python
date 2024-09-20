# Retornando valores
# Para retornar um valor, utilizamos a palavra "return".
# Toda função Python retorna "None" por padrão
# Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print("Olá Mundo!")


print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))
print(func_3()) # quando não tem return sempre ira retornar None