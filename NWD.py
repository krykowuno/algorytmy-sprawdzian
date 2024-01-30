def NWD(x,y):
    while x != y:
        if x>y:
            x=x-y
        elif x<y:
            y=y-x
    return x
def NWD_d(x,y):
    while x!=0 and y!=0:
        if x>y:
            x=x%y
        elif x<y:
            y=y%x
    if x != 0:
        return x
    else:
        return y

x=int(input("Podaj x: "))
y=int(input("Podaj y: "))
print(NWD_d(x,y))

