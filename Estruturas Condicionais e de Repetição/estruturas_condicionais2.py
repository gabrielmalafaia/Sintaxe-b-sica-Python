import sys

maior_idade = 18
idade_especial = 17

idade = int(input("Informe a sua idade: "))

if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH")
else:
    print("Menor de Idade, não pode tirar a CNH")


if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH")
elif idade == idade_especial:
    print("Pode fazer aula teórica, mas não pode fazer aula prática")
else:
    print("Menor de Idade, não pode tirar a CNH")
