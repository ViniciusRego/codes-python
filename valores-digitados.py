numeros = []

for i in range(5):
    numero = int(input("\nDigite um numero inteiro:"))
    numeros.append(numero)

for i in range(len(numeros)):
    if i==0:
         print(f"\nNumero {i+1}: {numeros[i]}")
    else:
         print(f"Numero {i+1}: {numeros[i]}")
