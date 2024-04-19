def rosnący(x):
    p=0
    for i in range(1,len(x)):
        if x[i]>x[i-1]:
            p+=1
    if p==len(x):
        return True
    else:
        return False

def malejący(x):
    p=0
    for i in range(1,len(x)):
        if x[i]<x[i-1]:
            p+=1
    if p==len(x):
        return True
    else:
        return False

plik=open("pi.txt","r")
linijki=plik.readlines()
wyrazy=[]
fragmenty=[]
for linijka in linijki:
    linijka=linijka.strip()
    wyrazy.append(linijka)

for i in range(1,len(wyrazy)):
    fragmenty.append(wyrazy[i-1]+wyrazy[i])
ciagi=[]
for i in range(2,len(fragmenty),3):
    ciagi.append(fragmenty[i-2]+fragmenty[i-1]+fragmenty[i])

for i in ciagi:
    if rosnący(i[:3]):





