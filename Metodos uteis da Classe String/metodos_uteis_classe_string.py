#Conhecer métodos úteis para manipular objetos do tipo string, como interpolar valores de variáveis
#Entender como funciona o fatiamento.

# A Classe string do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar.
# Em algumas linguagens manipular sequências de caracteres não é um trabalho trivial, porém, em Python
# esse trabalho é muito simples.

# Maiúscula, minúscula e título

curso = "pytHon"

print(curso.upper()) # Maiúsucula
print(curso.lower()) # Minúscula
print(curso.title()) # Primeira letra Maiúscula

# Eliminando espaços em branco metodo "strip()"

curso = "   Python  "

print(curso.strip() + ".") # Retira todos os espaços em branco
print(curso.lstrip() + ".")# Remove espaço da esquerda
print(curso.rstrip() + ".")# Remove espaço da direita


# Junções e centralização

curso = "Python"

print(curso.center(10))
print(curso.center(10, "#")) # primeito argumento(número de caraceteres), segundo(caracter que quer adicionar, se não colocar nada ele adiciona espaço)
print(".".join(curso))# Junção define o "caracter" que quer juntar.join, passa a string iterável
print("-".join(curso))