def selectionsort(a):
    for i in range(len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]
    return a


tab=[20,43,1,4,0,8,23,2,5]

print("przed sortowaniem:")
print(tab)
print("po sortowaniu:")
print(selectionsort(tab))