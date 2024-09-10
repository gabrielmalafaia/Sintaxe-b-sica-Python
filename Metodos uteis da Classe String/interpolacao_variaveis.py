# Em Python 3 temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal "%"
# A segunda é utilizando o método "format()"
# A Terceira e última é utilizando "f string"

# A primeira forma não é atualmente recomendada e seu uso em Python 3 é raro
# Por esse motivo iremos focar nas 2 últimas.

# Old style %

nome = "Gabriel"
idade = 25
profissao = "Analista de Dados"
linguagem = "Python"

print("Olá meu nome é %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))


# Método format

# formato parecido com old school o que muda é a definição da variável, mas tem os mesmo problemas
print("Olá meu nome é {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

# usando o mesmo método só definindo o número do indice da variável, zero based, a vantagem é que não precisa definir a variavel várias vezes
# os outros modelos precisa definir a variável várias vezes
print("Olá meu nome é {2}. Eu tenho {3} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, nome, idade))

# você define o que quer passar e na aba de argumento do format vc define a string que representa cada colchete com os argumento.
print("Olá meu nome é {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(linguagem=linguagem, profissao=profissao, nome=nome, idade=idade))

# usando dicionário

dados = {"nome": "Gabriel", "idade": 25, "profissao": "Analista de Dados", "linguagem": "Python"}
print("Olá meu nome é {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**dados))

# f-string

# não precisa colocar .format no final da string, só basta mencionar a váriavel

print(f"Olá meu nome é {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# Formatar string com f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")# voce define o width que no caso é zero e quantos caracteres
print(f"Valor de PI: {PI:10.2f}")# aqui foi definido o width de 10 o que adiciona espaços em branco e 2 caracteres
# o "f no final {PI:.2f}" define que é um float