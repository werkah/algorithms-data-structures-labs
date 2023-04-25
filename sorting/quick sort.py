def partition(a,l,r):
    pivot=a[r]
    i=l-1
    for j in range (l,r):
        if a[j]<=pivot:
            i+=1
            a[i],a[j]=a[j],a[i]
            print(a[i],a[j])
    a[i+1],a[r]=a[r],a[i+1]
    return i+1

def quicksort(a,l,r):
    if l<r:
        q=partition(a,l,r)
        quicksort(a,l,q-1)
        quicksort(a,q+1,r)
    return a

tab=[45,7,26,15,10,30,37,5,31,17]
n=len(tab)
print("przed sortowaniem:")
print(tab)
print("po sortowaniu:")
print(quicksort(tab,0,n-1))