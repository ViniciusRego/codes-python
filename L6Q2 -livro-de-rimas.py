def buscar_livro(estantes):
    for estante, livros in enumerate(estantes, start=1):
        for posicao, livro in enumerate(livros, start=1):
            if livro == "Livro de Rimas":
                return f"Og Loc, o livro ta na estante {estante}, na posicao {posicao}"
    
    return "Og Loc, o livro nao esta aqui!"


def main():
    num_estantes = int(input())
    estantes = []

    for a in range(num_estantes):
        num_livros = int(input())
        livros = []

        for b in range(num_livros):
            livro = input()
            livros.append(livro)

        estantes.append(livros)

    if len(estantes) == 0:
        print("Nao tem livros por aqui")
    else:
        resultado = buscar_livro(estantes)
        print(resultado)


if __name__ == "__main__":
    main()
