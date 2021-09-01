t = int(input())
res = []
for tc in range(t):
    n = int(input())
    items = list(map(int,input().split()))[:n]
    i = 0
    max = 0
    itemType = items[0]
    while i<n:
        c = 1
        j=i+1
        while j<n:
            if items[i]==items[j] and j!=i+1:
                c+=1
                if j<n-1 and items[j]==items[j+1]:
                    j+=1
            j+=1
        if max<c:
            max=c
            itemType = items[i]
        i+=1
    res.append(itemType)
for tc in range(t):
    print(res[tc])