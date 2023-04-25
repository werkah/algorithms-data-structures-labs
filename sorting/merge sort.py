def merge(a,l,q,r):
    n1=q-l+1
    n2=r-q
    L=[0]*(n1)
    R=[0]*(n2)
    for i in range(n1):
        L[i]=a[l+i]
    for j in range(n2):
        R[j] = a[q+j+1]
    i,j,k=0,0,l
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
        k+=1
    while i<n1:
        a[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        a[k]=R[j]
        j+=1
        k+=1

def mergesort(a, l, r):
    if l<r:
        q=(l+r)//2
        mergesort(a,l,q)
        mergesort(a,q+1,r)
        merge(a,l,q,r)
    return a

tab=[20,43,1,4,0,8,23,2,5]
print("przed sortowaniem:")
print(tab)
print("po sortowaniu:")
print(mergesort(tab,0,len(tab)-1))