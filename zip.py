a=[10,20,30,40]
b=[500,600,700,800]
for x,y in zip(a,b[::-1]):
    print(x,y)
