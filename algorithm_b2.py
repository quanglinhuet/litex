def f(x,y):
    temp =y
    line_to_1=[]
    distance=[]
    line_to_1.append(y)
    while temp!=1:
        if temp%2 ==0:  temp//=2
        else:  temp+=1  
        line_to_1.append(temp)
    count=0
    minDistance=1000000000
    indexInLine=0
    for i in range(len(line_to_1)):
        if x>line_to_1[i] :
            distance.append(x-line_to_1[i])
            if x-line_to_1[i]<minDistance:
                minDistance=x-line_to_1[i]
                indexInLine=i
        else: distance.append(-1)
    print('Min step: '+str(minDistance+indexInLine))
    way=[]
    for i in range(x,line_to_1[indexInLine],-1):
        way.append(i)
    for i in line_to_1[indexInLine::-1]:
        way.append(i)
    print('Way: '+str(way))
f(3,51)
