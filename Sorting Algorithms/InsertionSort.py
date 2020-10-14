def insertion_sort(x):
    for i in range(len(x)):
        key=x[i]
        j=i-1
        while j>=0 and key<x[j]:
            x[j+1]=x[j]
            j=j-1
        x[j+1]=key 
        
x=list(map(int,input().split()))
insertion_sort(x,)
print(x)
