def countingsort(a):
    n=len(a)
    b=[0]*n
    max_el=int(max(a))
    c=[0]*(max_el+1)
    for i in range(n):
        c[a[i]]+=1
    for i in range(1, max_el+1):
        c[i]+=c[i-1]
    i=n-1
    while i>=0:
        b[c[a[i]]-1]=a[i]
        c[a[i]]-=1
        i-=1
    return b


tab=[0,4,1,4,0,8,2,2,5]
print("przed sortowaniem:")
print(tab)
print("po sortowaniu:")
print(countingsort(tab))