# Fatiamento de strings é uma técnica utilizada para retornar substring(partes da string original)
# Informando inicio (start), fim (stop) e passo (step): [start: stop[,step]].

nome = "Gabriel Matheus da Silva Malafaia"
cpf = "464.072.178-14"

print(nome[3]) # como está defini só o [start] ele pega só um caratere
print(nome[-2]) # Seleciono de trás pra frente
print(nome[:7]) #se não definir o start ele irá começar do inicio da string
print(nome[8:]) # defini o start mas não fim
print(nome[8:15]) # defini onde começar[start] e onde parar[stop]
print(nome[0:34:2])# defini para começar[start] do inicio, parar no fim[stop], e [step], de quanto em quanto quero tirar da string
print(nome[:]) # Ele retorna astring inteira
print(nome[::-1]) # Para espelhar a string, mostra a string ao inverso

print(cpf[:3] + cpf[4:7] + cpf[8:11] + cpf[12:14])