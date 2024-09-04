# Como o interpretador Python utiliza a indentação do código para delimitar os blocos de comandos.
# Indentar código é uma forma de manter o código fonte mais legivel e manutenível. Mas em Python ela exerce
# um segundo papel, através da indentação o interpretador consegue determinar onde um bloco de comando
# inicia e onde ele termina.

# Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem. Nesse
# documento é indicado utilizar 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco
# adicionamos 4 novos espaços em branco.

# Bloco em Python
def sacar(self, valor: float): # inicio do bloco método
    
    if self.saldo >= valor: # Inicio do bloco if
        self.saldo -= valor
    
    # fim do bloco if
# fim do bloco do método
    

# Isso não funciona em Python o interpretador não lê

# def sacar(self, valor: float): # inicio do bloco método
# if self.saldo >= valor: # Inicio do bloco if
# self.saldo -= valor

# fim do bloco if
# fim do bloco do método

# EXEMPLO 2

def sacar(valor):
    
    saldo = 500
    
    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(1000)

# O código não funcionao sem indentação em blocos, se usar : para iniciar um bloco é obrigatório indentar
# em blocos