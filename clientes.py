import dados
from utils import titulo


def cadastrar_cliente():
    titulo("Cadastrar Cliente")

    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")

    cliente = {
        "nome": nome,
        "cpf": cpf
    }

    dados.clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    titulo("Lista de Clientes")

    if len(dados.clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in dados.clientes:
        print(f"Nome: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}")
        print("-" * 30)
