def idol(x):
    znaj=[]
    idl=[]
    for a in x:
        for i in range(len(a)):
            if a[i]==1:
                znaj.append(i)
            else:
                continue

    if znaj.count(najczesciej(znaj))==len(x)-1:
        for b in x:
            if b.count(0)==len(b)-1:
                idl.append(b)
        if len(idl)!=0:
            if x[najczesciej(znaj)]==idl[0]:
                return idl[0]
        else:
            return 'brak idola'


    else:
        return "brak idola"

def najczesciej(x):
    najcz=x[0]
    listapom=0
    for i in x:
        if x.count(i)>listapom:
            listapom=x.count(i)
            najcz=i
    return najcz


def lider(x):
    najcz=[]
    listapom=0
    for i in x:
        if x.count(i)>listapom:
            listapom=x.count(i)
            najcz.append(i)
    print(x.count(najcz[0]))
    print(len(x))
    if int(x.count(najcz[0]))>len(x)/2:
        return najcz[0]
    else:
        return "brak lidera"

lista=[['',1,0],[0,'',0],[1,1,'']]
print(idol(lista))

l=[2,3,4,5,6,7,7,7,7,7,7,7,8]

