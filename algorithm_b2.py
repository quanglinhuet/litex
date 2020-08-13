def f(x,y):
    s=str(y)
    count=0
    while y>x:
        y=y//2 if y%2==0 else y+1
        count+=1
        s= str(y)+' '+ s
        if y<x: 
            count =count + x-y
            for i in range(y+1,x+1): s= str(i)+' '+s
    print('Step: '+ str(count)+'\n Way: '+s)
f(3,51)
