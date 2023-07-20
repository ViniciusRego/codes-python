
answer = str()
doisAnos = []
outras = []
count = 0
while answer != 'não':
    num = int(input())
    answer = input().lower()
    if num <= 2:
        doisAnos.append(num)
    elif num > 2:
        outras.append(num)
somaDoisANos = (len(doisAnos) * 9) * 30
somaOutras = (len(outras) * 6) * 30
somaTotal = somaOutras+somaDoisANos
while somaTotal > 0:
    somaTotal-=100
    count+=1
print(count)
if somaTotal < 0:
    print(somaTotal*-1)
else:
    print(somaTotal)