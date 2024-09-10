#O "if" ternário permite escrever uma condição em uma única linha. Ele é  composto por três partes
#A primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica
#E a terceira parte é o retorno caso a expressão não seja atendida.

saldo = 1000
saque = float(input("Digite o valor para saque:"))

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")
