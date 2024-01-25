def horner(x,y):
    x=x.strip().split()
    wynik=int(x[0])
    for i in range(1,len(x)):
        wynik=(wynik*y)+int(x[i])
    return wynik

def miejscezerowe(a,b,x):
    if horner(x,a)==0:
        return a
    elif horner(x,b)==0:
        return b
    else:
        while not abs(a-b)<=0.00001:
            srodek=(a+b)/2
            if horner(x,srodek)==0:
                return srodek
            else:
                if horner(x,a)*horner(x,srodek)<0:
                    b=srodek
                else:
                    a=srodek

        return (a+b)/2
x=input('podaj wspołczynniki: ')
print(miejscezerowe(-10,10,x))