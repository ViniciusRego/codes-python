def main():
    # Leitura da quantidade de alunos
    n = int(input())

    # Lista para armazenar os dados dos alunos
    alunos = []

    # Leitura dos dados dos N alunos
    for i in range(n):
        matricula, nome, nota = input().split("-")
        matricula = int(matricula)
        nota = float(nota)
        alunos.append((matricula, nome, nota))

    # Cálculo da média das notas
    media = sum(nota for i, i, nota in alunos) / n

    # Separação dos alunos com nota abaixo da média e acima ou igual à média
    abaixo_media = []
    acima_ou_igual_media = []
    for matricula, nome, nota in alunos:
        if nota < media:
            abaixo_media.append((matricula, nome, nota))
        else:
            acima_ou_igual_media.append((matricula, nome, nota))

    # Ordenação dos alunos acima ou igual à média pela nota e matrícula
    acima_ou_igual_media.sort(key=lambda x: (x[2], x[0]))

    # Impressão dos resultados
    print("Alunos abaixo da media:")
    for matricula, nome, nota in abaixo_media:
        print(f"Matricula: {matricula} Nome: {nome} Nota: {nota:.1f}")

    print("Alunos iguais ou acima da media:")
    for matricula, nome, nota in acima_ou_igual_media:
        print(f"Matricula: {matricula} Nome: {nome} Nota: {nota:.1f}")

    print(f"Media = {media:.2f}")


if __name__ == "__main__":
    main()
