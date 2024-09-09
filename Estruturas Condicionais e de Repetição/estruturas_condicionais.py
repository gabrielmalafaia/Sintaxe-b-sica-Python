import sys

#A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas 
#são atendidas.

#If

#Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra
#reservada "if". O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes
#no bloco de código do if serão executadas.

#EXEMPLO 1

saldo = 2000.0
saque = float(input("informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque")

if saldo < saque:
    print("Saldo insuficiente!")


# If/esle

#Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else.
#Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado.
#Caso contrário o boco de código do else será executado.

#EXEMPLO 2

saldo = 2000.0
saque = float(input("informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque")

else:
    print("Saldo insuficiente!")

# If/elif/else

#Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra "elif".
#O "elif" é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro
#o bloco de código do elif será executado. Não existe um número máximo de "elifis" que podemos utilizar,
#porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código.

#EXEMPLO 3

opcao = int(input("Informe uma opção: [1] Sacar /n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o Extrato...")

else:
    sys.exit("Opção inválida")