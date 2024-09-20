# Escopo local e escopo global
# Python trabalha com escopo local e global, dentro do bloco da função o escopo é local
# Portanto alterações ali feitas em objetos imutáveis serão perdidos quando o método terminar
# Para usar objetos globais utilizamos a palavra chave "global", que informa ao interpretador que a
# variável que está sendo manipulada no escopo local é global.

# ESSA NÃO É UMA BOA PRÁTICA E DEVE SER EVITADA.

# Exemplo

salario = 2000 # É uma variável do escopo global por que está na raiz do programa
# Não está dentro de um função

def salario_bonus(bonus, lista):
    global salario # Chamei uma variável global para dentro do escopo local da função
    # sem declara o global não é possível utilizar a variável
    lista_aux = lista.copy() # A lista é um objeto imutável então deve se fazer uma cópia para alterar o valor dela
    lista_aux.append(2)
    print(f"Lista aux = {lista_aux}")
    salario += bonus
    return salario


lista = [1]
print(lista)
print(salario_bonus(500, lista))


