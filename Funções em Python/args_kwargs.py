# Podemos combinar parâmetros obrigatórios com args e kwargs.
# Quando esses são (*args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente

def exibir_poema(data_extenso, *args, **kwargs): # O nome não importa o que importa é os "* **" um * para args(lista) e dois ** Kwargs(dicionário)
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

    # Irá exibir uma variável que recebe três parâmetros assim como a função pede usando f string para receber os parâmetros
    # Primeiro argumento tem que receber uma data por extenso
    # variável texto segundo argumento um (args) vai concatenar uma quebra de linha usando .join recebendo o args
    # Então todos args irá seguir de uma quebra de linha
    # Terceiro argumento representado pela vairavel meta_dados que é um kwargs, irá começar quando houver
    # um argumento com chave=valor, fará uma quebra de linha concatenado com o .join
    # usando f string recebe uma variável que irá receber o texte em .titel, com a inicial maiuscula
    # essa variável irá receber um {valor} que será deifinido quando a função for chamada
    # o for chave, valor in kwargs.items() é pra dizer que todos esse argumento é um dicionário


# Todo primeiro argumento será o parâmetro "data_extenso", após isso todo argumento colocado será um *args
# o python só irá a reconhecer um **kwargs quando aparecer um argumento chave=valor
# lá no código inicia um kwargs em (autor="Tim Peters")

exibir_poema(
    "Sexta-feira, 26 de Agosto de 2022",
    "Zen of Python", 
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than neers.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters", 
    ano=1999)
