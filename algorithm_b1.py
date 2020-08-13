a=[1,2,3,4,5,6,7,8,9]
d=['x','x','x','x','x','x','x','x']


def check():
    sumA=0
    aIndex=0
    temp=a[0]
    temp_o='+'
    for i in d:
        aIndex+=1
        if i in ['+','-']: 
            sumA=sumA+temp if temp_o=='+' else sumA-temp
            temp=a[aIndex]
            temp_o=i
        else:
            temp = int(str(temp)+str(a[aIndex]))
    sumA=sumA+temp if temp_o=='+' else sumA-temp
    return True if sumA==100 else False
        

def f(deep):
    if deep ==8:
        if(check()): 
            s=''
            for i in range(8):
                s+=str(a[i])+d[i]
            s+=str(a[8])+'=100'
            print(s)
    else:
        for i in ['+','-','']:
            d[deep]=i
            f(deep+1)
            d[deep]='x'

f(0)