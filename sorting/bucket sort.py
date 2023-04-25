def insertionsort(bucket):
    for i in range (1,len(bucket)):
        var=bucket[i]
        j=i-1
        while (j>=0 and var<bucket[j]):
            bucket[j+1]=bucket[j]
            j=j-1
        bucket[j+1]=var
    return bucket

def bucketsort(a):
    n=len(a)
    b=[i*[] for i in range(n)]
    for j in a:
        idx=int(10*j)
        b[idx].append(j)
    for i in range(n):
        b[i]=insertionsort(b[i])
    k=0
    for i in range(n):
        for j in range(len(b[i])):
            a[k]=b[i][j]
            k+=1
    return a

tab=[.24,.43,.15,.47,.04,.81,.20,.23,.56]
print("przed sortowaniem:")
print(tab)
print("po sortowaniu:")
print(bucketsort(tab))