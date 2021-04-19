arr = list(map(int,input().rstrip().split()))
sumlist= []
for i in range(len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i == j:
            continue
        else:
            sum = sum + arr[j]
    sumlist.append(sum)
print(sumlist)
sumlist.sort()
print(sumlist[0])
print(sumlist[-1])
    
        