def selection_sort(x,n):
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if(x[min_index]>x[j]):
                min_index=j
        x[i],x[min_index]=x[min_index],x[i]
        
        
x=list(map(int,input().split()))
n=len(x)
selection_sort(x,n)

print(x)
