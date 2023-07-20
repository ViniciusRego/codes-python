moedasMario = int(input())
verde = list(map(int,input().split()))
vermelho = list(map(int,input().split()))
azul = list(map(int,input().split()))
amarelo = list(map(int,input().split()))
listYoshi = []
listPreferencia = []
CBverde = CBvermeho = CBazul = CBamarelo = indexMAXnum =  0
CBverde = verde[1] / verde[0]
CBvermelho = vermelho[1] / vermelho[0]
CBazul = azul[1] / azul[0]
CBamarelo = amarelo[1] / amarelo[0]
if verde[0] <= moedasMario:
    listYoshi.append('Verde')
    listPreferencia.append(CBverde)
if vermelho[0] <= moedasMario:
    listYoshi.append('Vermelho')
    listPreferencia.append(CBvermelho)
if azul[0] <= moedasMario:
    listYoshi.append('Azul')
    listPreferencia.append(CBazul)
if amarelo[0] <= moedasMario:
    listYoshi.append('Amarelo')
    listPreferencia.append(CBamarelo)
maxNUM = 0
for x in range(len(listPreferencia)):
    if x == 0:
        maxNUM = listPreferencia[x]
        indexMAXnum = x
    elif listPreferencia[x] > maxNUM:
        maxNUM = listPreferencia[x]
        indexMAXnum = x
if len(listPreferencia) == 0:
    print('Acho que vou a pe :(')
else:
    if (maxNUM-1) > CBverde:
        print(listYoshi[indexMAXnum])
    elif CBverde not in listPreferencia:
        print(listYoshi[indexMAXnum])
    else:
        print(listYoshi[0])