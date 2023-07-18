frase = input().lower()
letra = input().lower()
caracters = ['!','@','$','#','-','_',',','&','.']
contadorLetra = letrasTotal = 0
for i in frase:
    if i == letra:
        contadorLetra+=1
    if i != ' ' and i not in caracters:
        letrasTotal+=1
print(contadorLetra)
percentual = (contadorLetra/letrasTotal) * 100
print(f'{percentual:.2f}%')

