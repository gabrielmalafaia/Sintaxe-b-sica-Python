# Criação e acesso aos dados

# Um dicionário é um conjunto não-ordenado de pares "chave:valor"
# Onde as chaves são únicas em uma dada instância do dicionário.
# Dicionários são delimitados por chaves: {}ou "dict" e contém uma lista de pares
# "chave:valor" separada por vírgulas

# Exemplo
# Um dicionário recebe pares, chave:valor


pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28) # Usando o construtor "dict"

pessoa["telefone"] = "1234-5678" # Adicionando uma nova chave

# Acessando aos dados

dados = {"nome": "Gabriel", "idade": 25, "telefone": "1234-5678"}

dados["nome"] # Gabriel
dados["idade"] # 25
dados["telefone"] # 1234-5678

# Alterando/Sobrescrevendo valores

dados["nome"] = "Gabriely"
dados["idade"] = 25
dados["telefone"] = "8765-4321"

dados # {'nome': 'Gabriely', 'idade': 25, 'telefone': '8765-4321'}

# Dicionários aninhados

# Estruturas aninhadas são estruturas dentro de outra, vimos em listas e tuplas

# Dicionários podem armazenar qualquer tipo de objeto Python como valor,
# Desde que a chave para esse valor seja um objeto imutável como (strings e números)

# É uma ferramenta muito poderosa, usado muito para banco de dados

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
    "gabriel@gmail.com": {"nome": "Gabriel", "telefone": "1346-2356"},
    "gabriely@gmail.com": {"nome": "Gabriely", "telefone": "8765-4321"},
    "maite@gmail.com": {"nome": "Maite", "telefone": "8956-7845", "extra": {"a": 1}},
}
# print(contatos)

# Acessando um dado especifico
contatos["guilherme@gmail.com"]["telefone"] # "1234-5678"

extra = contatos["maite@gmail.com"]["extra"]["a"]
# print(extra)

# Iterar dicionários

# A forma mais comum para percorrer os dados de um dicionário é utilizando o comando for

# Meu teste

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
    "gabriel@gmail.com": {"nome": "Gabriel", "telefone": "1346-2356"},
    "gabriely@gmail.com": {"nome": "Gabriely", "telefone": "8765-4321"},
    "maite@gmail.com": {"nome": "Maite", "telefone": "8956-7845"},
}

for contato in contatos["gabriel@gmail.com"]["telefone"]:
    print(contato)

print("=" * 100)

for contato in contatos:
    print(contato)

print("=" * 100)

for indice, contato in enumerate(contatos):
    print(f"{indice}:{contato}")

# Exemplo da aula
print("=" * 100)

for chave in contatos:
    print(chave, contatos[chave])

# A melhor forma a ser usada é o metodo items, que retorna uma listas de tuplas
# Tem o mesmo resultado que a declaração acima, só que mais limpo, mais intuitivo e legível

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)   
