def potegowanie(lista):
    lista=lista.strip().split()
    potęga=int(lista[1])
    x=int(lista[0])
    potega=bin(potęga)[2:]
    potega=potega[::-1]
    wynik=1
    podstawa=x
    l=1
    for i in potega:
        l+=1
        if int(i)==0:
            podstawa*=podstawa
        elif int(i)==1:
            wynik*=podstawa
            podstawa*=podstawa

    return wynik, "liczba mnożeń "+str(l)

plik=open('potegowanie.txt','r')
linijki=plik.readlines()
for linijka in linijki:
    print(potegowanie(linijka))
