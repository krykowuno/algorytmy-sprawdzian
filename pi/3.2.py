plik=open("pi.txt","r")
linijki=plik.readlines()
wyrazy=[]
fragmenty=[]
for linijka in linijki:
    linijka=linijka.strip()
    wyrazy.append(linijka)

for i in range(1,len(wyrazy)):
    fragmenty.append(wyrazy[i-1]+wyrazy[i])
p=0
lista=["0"+str(i) for i in range(100) if i<10]
lista1=[str(i) for i in range(100) if i>9]
liczby=lista+lista1
odp=[]
odpowiedzi=[]
for i in liczby:
    odp.append(fragmenty.count(i))
maks = 0
mini=9000
minimum=[]
maximum=[]
for i in range(len(odp)):
    if int(odp[i])>maks:
        maks=int(odp[i])
        maximum.clear()
        maximum.append(liczby[i])
        maximum.append(odp[i])
    if int(odp[i])<mini:
        mini=int(odp[i])
        minimum.clear()
        minimum.append(liczby[i])
        minimum.append(odp[i])
print(maximum)
print(minimum)



