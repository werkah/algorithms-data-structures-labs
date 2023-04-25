#Weronika Hilaszek

def countingsort(a, pos):
    n=len(a)
    b=[0]*n
    c=[0]*10
    for i in range(n):
        idx=a[i]//pos
        c[idx%10]+=1
    for i in range(1, 10):
        c[i]+=c[i-1]
    i=n-1
    while i>=0:
        idx=a[i]//pos
        b[c[idx%10]-1]=a[i]
        c[idx%10]-=1
        i-=1
    for i in range(n):
        a[i]=b[i]


def radixsort(a):
    max_el=max(a)
    pos=1
    while max_el//pos>0:
        countingsort(a,pos)
        pos*=10
    return a

tab=[201,434,123,454,530,128,223,243,523]
print("przed sortowaniem:")
print(tab)
print("po sortowaniu:")
print(radixsort(tab))