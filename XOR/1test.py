plik=open("bin.txt")
linijki=plik.readlines()
odp=[]
for linijka in linijki:
    odpowiedzi = ""
    linijka=linijka.strip()
    p=linijka
    p2=int(p,2)//2
    p2=bin(p2)[2::]
    if len(p)==len(p2):
        for i in range(len(p)):
            if p[i]==p2[i]:
                odpowiedzi+="0"
            else:
                odpowiedzi+="1"
    else:
        for i in range(len(p)-len(p2)):
                p2=p2[::-1]
                p2=p2+"0"
                p2=p2[::-1]
        for i in range(len(p)):
            if p[i]==p2[i]:
                odpowiedzi+="0"
            else:
                odpowiedzi+="1"
    print(odpowiedzi)

