import dados
from utils import titulo


def cadastrar_filme():
    titulo("Cadastrar Filme")

    nome = input("Título do filme: ")
    genero = input("Gênero: ")
    ano = input("Ano do filme: ")

    filme = {
        "titulo": nome,
        "genero": genero,
        "ano": ano,
        "disponivel": True
    }

    dados.catalogo.append(filme)

    print("Filme cadastrado com sucesso!")


def listar_catalogo():
    titulo("Catálogo de Filmes")

    if len(dados.catalogo) == 0:
        print("Nenhum filme cadastrado.")
        return

    for filme in dados.catalogo:

        status = "Disponível" if filme["disponivel"] else "Indisponível"

        print(f"Título: {filme['titulo']}")
        print(f"Gênero: {filme['genero']}")
        print(f"Ano: {filme['ano']}")
        print(f"Status: {status}")
        print("-" * 30)


def reservar_filme():
    titulo("Fila de Reservas")

    nome_filme = input("Digite o título do filme: ")
    nome_cliente = input("Digite o nome do cliente: ")

    # Verifica se o cliente existe
    cliente_existe = False

    for cliente in dados.clientes:
        if cliente["nome"].lower() == nome_cliente.lower():
            cliente_existe = True
            break

    if not cliente_existe:
        print("Cliente não cadastrado.")
        return

    # Procura o filme
    for filme in dados.catalogo:
        if filme["titulo"].lower() == nome_filme.lower():

            reserva = {
                "cliente": nome_cliente,
                "filme": nome_filme
            }

            # FIFO
            dados.fila_reservas.append(reserva)

            print("Reserva registrada com sucesso!")
            return

    print("Filme não encontrado.")


def registrar_aluguel():
    titulo("Registrar Aluguel")

    if len(dados.fila_reservas) == 0:
        print("Nenhuma reserva na fila.")
        return

    reserva = dados.fila_reservas.pop(0)

    for filme in dados.catalogo:
        if filme["titulo"].lower() == reserva["filme"].lower():

            if filme["disponivel"]:
                filme["disponivel"] = False

                print(
                    f"{reserva['cliente']} alugou {filme['titulo']}"
                )
                return

            print("Filme indisponível.")
            return


def registrar_devolucao():
    titulo("Registrar Devolução")

    nome_filme = input("Digite o título do filme: ")

    for filme in dados.catalogo:
        if filme["titulo"].lower() == nome_filme.lower():

            filme["disponivel"] = True

            # LIFO
            dados.pilha_devolucoes.append(filme["titulo"])

            print("Devolução registrada com sucesso!")
            return

    print("Filme não encontrado.")


def ver_devolucoes():
    titulo("Pilha de Devoluções")

    if len(dados.pilha_devolucoes) == 0:
        print("Nenhuma devolução registrada.")
        return

    for filme in reversed(dados.pilha_devolucoes):
        print(filme)


def buscar_filme():
    titulo("Buscar Filme")

    busca = input("Digite o título do filme: ")

    for filme in dados.catalogo:
        if busca.lower() in filme["titulo"].lower():

            print("Filme encontrado!")
            print(f"Título: {filme['titulo']}")
            print(f"Gênero: {filme['genero']}")
            print(f"Ano: {filme['ano']}")
            return

    print("Filme não encontrado.")


def listar_por_genero():
    titulo("Filmes Disponíveis por Gênero")

    genero = input("Digite o gênero: ")

    encontrou = False

    for filme in dados.catalogo:
        if filme["genero"].lower() == genero.lower() and filme["disponivel"]:
            print(f"- {filme['titulo']}")
            encontrou = True

    if not encontrou:
        print("Nenhum filme disponível nesse gênero.")