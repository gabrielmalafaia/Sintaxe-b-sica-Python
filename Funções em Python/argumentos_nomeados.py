# Argumentos Nomeados
# Funções também podem ser chamadas usado argumentos nomeados da forma chave=valor.

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # Tem que tomar cuidado com a ordem dos valores inseridos
# deve ser sequêncial
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # deste modo é menos sucetível a erros
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # usando um dicionário

