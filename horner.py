def horner(x,y):
    x=x.strip().split()
    wynik=int(x[0])
    for i in range(1,len(x)):
        wynik=(wynik*y)+int(x[i])
    return wynik


x=input('podaj współczynniki po spacji: ')
y=int(input('podaj x:'))
print(horner(x,y))