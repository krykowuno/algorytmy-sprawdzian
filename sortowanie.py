
def kubełkowe(x):
    wynik=[]
    print(max(x))
    for i in range(min(x),max(x)+1):
        b=[a for a in x if a==i]
        if len(b)!=0:
            wynik.extend(b)
    return wynik

def zliczanie(x):
    wynik=[]
    slownik={}
    for a in x:
        if a not in slownik:
            slownik[a]=1
        else:
            slownik[a]+=1
    for i in range(min(x),max(x)+1):
        try:
            wynik.append(slownik[i]*str(i))
        except:
            continue
    return wynik

def babelkowe(x):
    for i in range(len(x)):
        for a in range(1,len(x)):
            if x[a-1]>x[a]:
                x[a],x[a-1]=x[a-1],x[a]
    return x

def wstawianie(x):
    for i in x:
        for a in range(len(x)):
            print(i,x[a])
            if i<x[a]:
                x.insert(a, i)
                x.remove(i)
                break
    return x

def pivot(x):
    if len(x)<=1:
        return x
    else:
        zpivot=x[-1]
        listaw=[i for i in x[:-1] if i>=zpivot]
        listam=[i for i in x[:-1] if i<zpivot]
        return pivot(listam) + [zpivot] + pivot(listaw)



x=[2,5,7,6,-12,4,1,6,12]
print(pivot(x))


