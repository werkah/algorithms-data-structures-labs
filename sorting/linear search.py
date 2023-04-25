def linearsearch(x,a):
    for i in range(len(a)):
        if a[i]==x:
            return i
    return ("nie ma takiej liczby")


tab=[0,1,2,4,5,8,20,23,43]
print("indeks szukanego elementu to:")
print(linearsearch(0,tab))