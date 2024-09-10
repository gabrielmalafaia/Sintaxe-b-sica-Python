#Podemos criar estruturas condicionais, annhadas, para isso basta adicionar estruturas "if/elif/else"
#dentro do bloco de código de estruturas if/elif/else.

conta_normal = False
conta_universitária = False

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente")

elif conta_universitária:
    
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")
        
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com seu gerente!")
