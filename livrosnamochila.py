peso_total = 0
livros = 0

print("Insira o peso dos livros:")

while True:
    peso = float(input())
    if peso + peso_total <= 18:
        peso_total += peso
        livros += 1
    else:
        break

print("Podem ser carregados", livros, "livros.")
