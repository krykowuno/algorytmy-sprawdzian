def potegowanie(lista):
    lista=lista.strip().split()
    potęga=int(lista[1])
    x=lista[0]
    potega=bin(potęga)[2:]
    potega=potega[::-1]
    podstawa=int(x)
    wynik=1
    l=1
    for i in potega:
        l+=1
        if int(i)==0:
            podstawa*=podstawa
        elif int(i)==1:
            wynik*=podstawa
            podstawa*=podstawa

    return str(lista[0])+"^"+str(lista[1])+"="+str(wynik),"liczba mnożeń"+ " "+ str(l)

plik=open('potegowanie.txt','r')
linijki=plik.readlines()
for linijka in linijki:
    wartosci=linijka.split()
    print(potegowanie(linijka)[0]+","+potegowanie(linijka)[1])


