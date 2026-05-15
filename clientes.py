from dados import clientes
from utils import titulo


def cadastrar_cliente():
    titulo("Cadastrar Cliente")

    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")

    cliente = {
        "id": len(clientes) + 1,
        "nome": nome,
        "telefone": telefone
    }

    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    titulo("Lista de Clientes")

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print(f"ID: {cliente['id']}")
        print(f"Nome: {cliente['nome']}")
        print(f"Telefone: {cliente['telefone']}")
        print("-" * 30)