def horner(x):
    x=x.strip().split()
    liczba=x[0]
    system=int(x[1])
    w = int(liczba[0])
    for a in range(1,len(liczba)):
        w=(system*w)+int(liczba[a])
    return w

plik=open('zamiana.txt','r')
linijki=plik.readlines()
for linijka in linijki:
    print(horner(linijka))
