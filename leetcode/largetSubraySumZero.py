arr = [1,2,-2,4,3,3,-10,12,-12,43]
size = len(arr)
k = 0
length = 0
current_len = 0
found = False
count = 0
for i in range(size):
    sum  = 0
    for j in range(i,size):
        sum += arr[j]
        if sum == k:
            count += 1             # for counting number of sub arrays whose sum equal to k.
            current_len = len(arr[i:j+1])
            found = True
        if current_len > length:
            length = current_len

if found :
    print(length)
    print("No. of sub arrays whose sum is k",count)
else:print(found)


