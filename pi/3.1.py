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
for i in fragmenty:
    if int(i)>90:
        p+=1
print(p)