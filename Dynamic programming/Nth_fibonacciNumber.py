#Recursive
def rfib(n):
    if n<0:
        print("Invalid Input")
    elif n<=1:
        return n
    else:
        return rfib(n-1)+rfib(n-2)
    
#Dynammic Programming Buttom up approach

def dfib(n):
    a=[0,1]
    for i in range(2,n+1):
        a.append(a[i-1]+a[i-2])
        
    return a[n]
    
#Top Down

def dfib1(n):
    a=[0,1]
    for i in range(n-1):
        a.append(-1)
    if n<=1:
        return n
    else:
        if a[n-1]==-1:
            a[n-1]=dfib1(n-1)
        if a[n-2]==-1:
            a[n-2]=dfib1(n-2)
    a[n]=a[n-2]+a[n-1]
    return a[n]

if __name__=="__main__":
    print(rfib(10))
    print(dfib(10))
    print(dfib1(10))
    
