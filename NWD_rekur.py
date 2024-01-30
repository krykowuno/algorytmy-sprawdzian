def NWD(x,y): #rekurencyjnie
    if x==y:
        return x
    if x>y:
        return NWD((x-y),y)
    elif x<y:
        return NWD(x,(y-x))

def fibonacci(x): #iteracyjnie
    a=0
    b=1
    if x==0:
        return 0
    if x>0:
        for i in range(0,x-1):
            a, b = b, a+b  ##zamiana zmiennych a i b na b i a+b
        return b

def fibonaccir(x):
    if x<3:
        return 1
    else:
        return fibonaccir(x-1)+fibonaccir(x-2)


x=int(input())

for i in range(2,x+1):
    a=fibonacci(i)/fibonacci(i-1)
    print(i,round(a,3))

