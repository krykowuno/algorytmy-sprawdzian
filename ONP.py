def notacja(x):
    s=[i for i in x ]
    stos=[]
    for a in s:
        try:
            stos.append(int(a))
        except:
            if a=='-':
                stos.append(int(stos[-2])-int(stos[-1]))
                del stos[-2]
                del stos[-2]
            elif a=='+':
                stos.append((int(stos[-2])+int(stos[-1])))
                del stos[-2]
                del stos[-2]
            elif a=='/':
                stos.append(int(stos[-2])/int(stos[-1]))
                del stos[-2]
                del stos[-2]
            elif a=='*':
                stos.append(int(stos[-2])*int(stos[-1]))
                del stos[-2]
                del stos[-2]
    return stos






print(notacja('23+45*-'))