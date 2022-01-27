def fac(x):
    m=1
    for i in range(1,x+1):
        m*=i
    return m
e=1
for h in range(1,101):
    d = fac(h)
    e = e+(1/d)
print(e)
