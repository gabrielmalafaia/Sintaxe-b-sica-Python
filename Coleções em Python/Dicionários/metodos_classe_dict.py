# Métodos da Classe "dict"

# {}.clear
# Ele apaga todos os valores de um dicionário


contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
    "gabriel@gmail.com": {"nome": "Gabriel", "telefone": "1346-2356"},
    "gabriely@gmail.com": {"nome": "Gabriely", "telefone": "8765-4321"},
    "maite@gmail.com": {"nome": "Maite", "telefone": "8956-7845"},
}

print(contatos)

print("=" * 100)


contatos.clear()
print(contatos)

print("=" * 100)

# {}.copy
# Igual aos metodos usados em outras coleções, ele copia os dados de um objeto para outro
# Usado quando você quer manipular uma coleção sem alterar os dados originais

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
    "gabriel@gmail.com": {"nome": "Gabriel", "telefone": "1346-2356"},
    "gabriely@gmail.com": {"nome": "Gabriely", "telefone": "8765-4321"},
    "maite@gmail.com": {"nome": "Maite", "telefone": "8956-7845"},
}

print(contatos)

copia_contatos = contatos.copy()

copia_contatos["guilherme@gmail.com"] = {"nome": "Gui"}

print("=" * 100)

print(contatos)
print(copia_contatos)

print("=" * 100)


contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
    "gabriel@gmail.com": {"nome": "Gabriel", "telefone": "1346-2356"},
    "gabriely@gmail.com": {"nome": "Gabriely", "telefone": "8765-4321"},
    "maite@gmail.com": {"nome": "Maite", "telefone": "8956-7845"},
}

print(contatos)

print("=" * 100)

# {}.fromkeys

# Ele cria chaves pra você em duas situações
# Quando você que criar uma chave no seu dicionário e não quer vincular nenhum valor
# Passa uma lista das chaves que você quer adicionar no seu dicionário
# A segunda opção é você criar um conjunto de chaves e colocar um valor padrão nela

contact = dict.fromkeys("nome", "telefone")
print(contact)

contact = dict.fromkeys(["nome", "telefone"], "none")
print(contact)

# {}.get
# Segunda forma de acessa dados dentro de um dicionário

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
}

# contatos["chave"] # KeyError, ele para o programa

# Utilizamos o metodo get, quando não temos certeza do que tem no dicionário

contatos.get("chave") # Quando ele não encontra a chave ele retorna 'None'
contatos.get("chave", {}) # Você pode definir um valor defaulta para o get, se ele não encontrar a chave
# Ele retorna um '{}' assim como definido nos argumentos
contatos.get("guilherme@gmail.com", {}) # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"}}
# Se encontra o valor dentro do dicionário, vai executar o que contem no dicionário citado

# {}.items
# Nos retorna uma lista

contatos.items() # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '1234-5678'})])

# {}.keys
# Retorna só as chaves do dicionário

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
}

contatos.keys() # dict_keys(['guilherme@gmail.com'])

# {}.pop
# Vai remover um valor do seu dicionário

contatos_pop = contatos.pop("guilherme@gmail.com") # Você pode passar um valor pra remover
print(contatos_pop)

# Se não existir um valor você pode pedir pra retornar algo igual no get

contatos_pop = contatos.pop("guilherme@gmail.com", "Valor não encontrado")
print(contatos_pop)

# {}.popitem
# Ele remove os itens sem precisar especificar, vai removendo um por um, e se o dicionário estive vazio
# Retorna erro

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
}
contatos_popitem = contatos.popitem()
print(contatos)

# {}.setdefault
# Se o atributo não existe no dicionário ele insere, se ja existir não faz nada

contatos = {"nome": "Guilherme", "telefone": "1234-5678"}

contatos.setdefault("nome", "Giovanna")
print(contatos)

contatos.setdefault("idade", 28)
print(contatos)

# {}.update
# Ele sobrescreve um valor do dicionário

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
}

contatos.update({"guilherme@gmail.com": {"nome":"Gui"}})
print(contatos)

contatos.update({"giovanna@gmail.com" : {"nome" : "Giovana", "telefone": "2255-8877" }})
print(contatos)

# {}.values

# Retorna somente os valores que estão nas chave

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
    "gabriel@gmail.com": {"nome": "Gabriel", "telefone": "1346-2356"},
    "gabriely@gmail.com": {"nome": "Gabriely", "telefone": "8765-4321"},
    "maite@gmail.com": {"nome": "Maite", "telefone": "8956-7845"},
}

contatos_values = contatos.values()
print(contatos_values) # dict_values([{'nome': 'Guilherme', 'telefone': '1234-5678'}, {'nome': 'Gabriel', 'telefone': '1346-2356'}, {'nome': 'Gabriely', 'telefone': '8765-4321'}, {'nome': 'Maite', 'telefone': '8956-7845'}])

# Método in

# Usado pra verificar se algum valor está presente em um dicionário

resultado = "gabriely@gmail.com" in contatos
print(resultado)

resultado = "george@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["gabriel@gmail.com"]
print(resultado)

resultado = "telefone" in contatos["maite@gmail.com"]
print(resultado)

# Método 'del'

# Metodo usado para remover um objeto especifico

del contatos["maite@gmail.com"]["telefone"]
print(contatos)

del contatos["guilherme@gmail.com"]
print(contatos)

# Se usar somente o del e o dicionario ele irá excluir o dicionário inteiro