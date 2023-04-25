def max_heapify(a,n,i):
    largest=i
    r=2*i+2
    l=2*i+1
    if l<n and a[i]<a[l]:
        largest=l
    else:
        largest=i
    if r<n and a[largest]<a[r]:
        largest=r
    if largest!=i:
        a[i],a[largest]=a[largest],a[i]
        max_heapify(a,n,largest)


def heapsort(a):
    n=len(a)
    for i in range(n//2,-1,-1):
        max_heapify(a,n,i)
    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        max_heapify(a,i,0)
    return a


tab=[20,43,1,4,0,8,23,2,5]
print("przed sortowaniem:")
print(tab)
print("po sortowaniu:")
print(heapsort(tab))