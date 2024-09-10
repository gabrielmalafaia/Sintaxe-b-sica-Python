# while True:
#     numero = int(input("Informe m número: "))

#     if numero == 10:
#         break

#     print(numero)

# O laço de repetição ira repetir até atender a condição de parada "break"

# for numero in range(100):
#     if numero == 50:
#         break

#     print(numero, end=" ")


# for numero in range(100):
#     if numero == 10:
#         continue # usa "continue" para fazer o inverso de break mas ele desvia de um valor que foi escolhido na lógica
#         # nesse caso ele irá pular o número 10 e vai continuar a sequencia definida pelo range
#     print(numero, end=" ")

# for numero in range(100):
#     if numero % 2 == 0:
#         continue
#     print(numero, end=" ")

while True:
    numero = int(input("Informe m número: "))

    if numero % 2 == 0:
        continue
            # se não tiver um break nesse caso ele criará um loop infinito
            # sempre deve utilizar o break antes do continue dependendo do caso
    if numero == 10:
        break

    print(numero)