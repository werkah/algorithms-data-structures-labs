def insertionsort(a):
    for j in range(1, len(a)):
        key=a[j]
        i=j-1
        while i>=0 and a[i]>key:
            a[i+1]=a[i]
            i=i-1
        a[i+1]=key
    return a


tab=[20,43,1,4,0,8,23,2,5]
print("przed sortowaniem:")
print(tab)
print("po sortowaniu:")
print(insertionsort(tab))