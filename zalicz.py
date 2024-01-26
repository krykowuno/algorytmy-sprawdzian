def potegowanie(lista):
    ##lista=lista.strip().split()
    potęga=lista[1]
    x=lista[0]
    potega=bin(potęga)[2:]
    potega=potega[::-1]
    print(potega)
    wynik=x
    for i in potega:
        if int(i)==0:
            wynik+=wynik
        elif int(i)==1:
            wynik*=x

    return wynik

plik=open('potegowanie.txt','r')
print(potegowanie([2,8]))
