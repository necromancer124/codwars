def move(lst):
    x=[]
    y=[]
    for i in lst:
        if(i==0):
            x.append(i)
        else:
            y.append(i)
    for i in x:
        y.append(i)
    return y
x=[1,2,3,0,4,5]
print(move(x))
