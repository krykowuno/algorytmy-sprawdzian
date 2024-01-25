def rekurencyjnie(x,k):
    if k==0:
        return 1
    if k==1:
        return x
    else:
        if k%2==0:
            return rekurencyjnie(x,k/2)*rekurencyjnie(x,k/2)
        else:
            return rekurencyjnie(x,k-1)*x

def binarnie(x,k):
    k=bin(k)[2::]
    k=k[::-1]
    wynik=1
    podstawa=x
    for i in k:
        if int(i)==0:
            podstawa*=podstawa
        elif int(i)==1:
            wynik*=podstawa
            podstawa *= podstawa
    return wynik


print(rekurencyjnie(2,14))
print(binarnie(2,14))