n = int(input())
arrayN = []
for i in range(n):
    num = int(input())
    arrayN.append(num)
xNum = int(input())
listNUM = str()
for v in arrayN:
    v = str(v)
    listNUM += v + ' '
print(f'[ {listNUM}]')

if len(arrayN) == 0:
    print('A lista estah vazia - nao eh possivel remover elemento')
else:
    listNUM2 = str()
    if xNum in arrayN:
        arrayN.remove(xNum)
        for b in arrayN:
            b = str(b)
            listNUM2 += b + ' '
        print(f'[ {listNUM2}]')
    else:
        print(f'Nao eh possivel remover o elemento {xNum}')
