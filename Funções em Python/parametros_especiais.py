# Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome.
# Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos
# possam ser passados, assim um desenvolvedor precisa apenas olhar para a definição da função
# para que possa determinar se os itens são passados por posição, por posição e nome, ou por nome

# Exemplo Só por posição se usa a /

def criar_carro(modelo, ano, placa, / , marca, motor, combustivel):
    # Tudo antes da barra não posso nomear o argumento na função, após a barra eu sou obrigado a chamar pelo nome
    # Veja como vai ficar quando vou chamar a função
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Uno", 2016, "AB3DEFG", "Fiat", "1.6", "Flex")
criar_carro("Uno", 2016, "AB3DEFG", marca="Fiat", motor="1.6", combustivel="Flex")
# Não é obrigado após a barra usar chave valor, pode optar por ser só por posição, mas o contrário não pode
# criar_carro(modelo="Uno", ano=2016, placa="AB3DEFG", marca="Fiat", motor="1.6", combustivel="Flex") #Inválido

# Só por palavra se usa *

def criar_carro_2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_2(modelo="Gol",ano="2015", placa="abc-1234".upper(), marca="Volkswagen", motor="2.0", combustivel="Gasolina")
# desse modo nãoé possível fazer por posição
# criar_carro_2("Gol", 1990, "ABC-1234", "Volkswagen", "2.0", "Flex") # Inválido

# Por Palavra e Posição (Híbrido)

def criar_carro_3(modelo, ano, placa, / , *, marca, motor, combustivel):
        # Antes da / por posição (modelo, ano, placa) e após o *  por nome (marca, motor, combustivel)
        # O inverso é inválido
        print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_3("Corsa", 2005, "ABC-1234", marca="Chevrolet", motor="1.4", combustivel="Alcool")

def criar_carro_4(modelo, ano, placa, / , marca, *, motor, combustivel):
      # O parâmetro que está entra a / e * agora é opcional
      print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_4("Corsa", 2005, "ABC-1234", marca="Chevrolet", motor="1.4", combustivel="Alcool")