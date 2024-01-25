def pierwiastek(x):
    a=1
    b=x
    while abs(b-a)>0.000001:
        d=(a+b)/2
        a=d
        b=x/a
    return (a+b)/2

print(pierwiastek(5))