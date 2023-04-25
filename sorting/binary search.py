def binarysearch(x,a):
    l=0
    r=len(a)-1
    while l<=r:
        mid=(l+r)//2
        if x<a[mid]:
            r=mid-1
        elif x>a[mid]:
            l=mid+1
        else:
            return mid
    return ("nie ma tej liczby")

tab=[0,1,2,4,5,8,20,23,43]
print("indeks szukanego elementu to:")
print(binarysearch(8,tab))