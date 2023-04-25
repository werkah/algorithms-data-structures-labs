#Weronika Hilaszek

def bubblesort(a):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a


tab=[20,43,1,4,0,8,23,2,5]
print("przed sortowaniem:")
print(tab)
print("po sortowaniu:")
print(bubblesort(tab))