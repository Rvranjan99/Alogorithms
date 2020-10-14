def bubble_sort(x):
    n=len(x)
    
    for i in range(n):
        flag=0
        for j in range(n-i-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
                flag=1
        if not flag:
            break
  
x=list(map(int,input().split()))

bubble_sort(x,)
print(x)
