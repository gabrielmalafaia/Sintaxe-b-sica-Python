# Strings de múltiplas linhas são definidas informando 3 aspas simples ou duplas durante a atribuição.
# Elas podem ocupar várias linhas do código, e todos os espaços em brancos são incluídos na string final.

# Strings de Multiplas Linhas / Strings Triplas

nome = "Gabriel"
linguagem = "Python"
mensagem = f"""
Olá meu nome é {nome}.
Eu estou aprendendo {linguagem}""" # Usar aspas simple '''mensagem''' tem o mesmo efeito das aspas duplas

print(mensagem)


print('''
   --------MENU---------
      
      1 - Depositar
      2 - Sacar
      3 - Extrato
      0 - Sair
    ----------------------
        Obrigado por usar nosso sistema !!!
''')

