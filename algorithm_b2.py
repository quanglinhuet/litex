def f(x,y):
    line_to_1=[y]
    while y!=1:
        y=y//2 if y%2==0 else y+1  
        line_to_1.append(y)
    minDistance=1000000000
    indexInLine=0
    for i in line_to_1:
        if x>i and x-i<minDistance:
            minDistance=x-i
            indexInLine=line_to_1.index(i)
    print('Min step: '+str(minDistance+indexInLine))
    way=[]
    for i in range(x,line_to_1[indexInLine],-1): way.append(i)
    for i in line_to_1[indexInLine::-1]: way.append(i)
    print('Way: '+str(way))
f(99,100)