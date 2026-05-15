# main.py

from clientes import (
    cadastrar_cliente,
    listar_clientes
)

from filmes import (
    cadastrar_filme,
    listar_catalogo,
    registrar_aluguel,
    registrar_devolucao,
    ver_devolucoes
)


def menu():
    print("\n========================================")
    print("      CineVerse - Locadora de Filmes     ")
    print("========================================")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Cadastrar filme")
    print("4 - Listar filmes")
    print("5 - Alugar filme")
    print("6 - Devolver filme")
    print("7 - Ver pilha de devoluções")
    print("0 - Sair")
    print("========================================")


def main():

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            cadastrar_filme()

        elif opcao == "4":
            listar_catalogo()

        elif opcao == "5":
            registrar_aluguel()

        elif opcao == "6":
            registrar_devolucao()

        elif opcao == "7":
            ver_devolucoes()

        elif opcao == "0":
            print("Saindo da locadora...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()