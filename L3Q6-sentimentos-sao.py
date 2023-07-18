num = int(input())
stock = []

for i in range(num):
    command = input().lower()
    if command == 'registro':
        product = input().split()
        if len(product) == 1:
            product1 = str()
            product1 += product[0]
            if product1 not in stock:
                print("Produto registrado com sucesso")
                stock.append(product1)
            else:
                print("Produto nao registrado")
        else:
            product2 = str()
            product2 += product[0]
            product2 += product[1]
            if product2 not in stock:
                print("Produto registrado com sucesso")
                stock.append(product2)
            else:
                print("Produto nao registrado")

     #elif command == 'venda':


    #elif command == 'recarga':


