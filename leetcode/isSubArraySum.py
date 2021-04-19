from itertools import accumulate

arr = [1,1,1]
ls = list(accumulate(arr))
k = 2
checker = set()
sum = 0
found = False
for i in arr:
    sum += arr[i]
    if sum-i == k:
        found = True
        break
if found:
    print(found)

