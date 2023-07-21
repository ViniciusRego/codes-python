num = input().split()
x = int(num[0])
y = int(num[1])
count=maxDiv=number=0
for i in range(1,y+1):
    for n in range(1,y+1):
        if i%n==0:
            count+=1
        if n==y:
            if i==x:
                maxDiv = count
                number = i
            elif count>maxDiv:
                maxDiv = count
                number = i
            count = 0
print(f'{number} {maxDiv}')