def hour_glass_sum(arr):
    max_sum = 0
    for i in range(4):              
        for j in range(4):
            Sum = 0
            for k in range(3):
                if k == 1:
                    sub_ar = arr[i+k]
                    mid = sub_ar[j:j+3]
                    Sum += mid[1]
                else:
                    sub_ar = arr[i+k]
                    Sum += sum(sub_ar[j:j+3])
            if max_sum < Sum :
                max_sum = Sum
    return max_sum

arr = []
for i in range(6):
    arr.append(list(map(int,input().strip().split())))



print(hour_glass_sum(arr))