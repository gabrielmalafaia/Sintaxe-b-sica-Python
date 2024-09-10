#O comando "for" é usado para percorrer um objeti iterável. Faz sentido usar "for" quando sabemos o número
# exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável

texto = input("Informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
else:
    print()
