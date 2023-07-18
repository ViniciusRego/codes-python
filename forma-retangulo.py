def retangulo(a,b,c,d):
    if ((a and b) > 0) and ((c and d) > 0):
        if (a==d and b==c):
            print('formam um retangulo')
        elif (a==b and c==d):
            print('formam um retangulo')
        elif (a==c and b==d):
            print('formam um retangulo')
        else:
            print('nao formam um retangulo')
    else:
        print('nao formam um retangulo')
    

a = int(input())
b = int(input())
c = int(input())
d = int(input())
retangulo(a,b,c,d)