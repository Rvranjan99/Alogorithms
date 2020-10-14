#Recursive
def b_search(a,key,l,r):
    if r>=l:
        mid=l + (r - l) // 2
        if a[mid]==key:
            return mid
        elif a[mid]>key:
            return b_search(a,key,l,mid-1)
        else:
            return b_search(a,key,mid+1,r)
    else:
        return -1
#iter   
def bs_iter(a,key):
    l=0
    r=len(a)-1
    while r>=l:
        mid=l+(r-l)//2
        if a[mid]==key:
            return mid
        elif a[mid]>key:
            r=mid-1
        else:
            l=mid+1
    return -1
a=[1,3,5,6,7,10]

a.sort()
x=bs_iter(a,14)
if x==-1:
    print("NOT FOUND")
else:
    print('found at index',x)
