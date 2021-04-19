def two_sum(arr,target):
    val = dict()
    for i in range(len(arr)):
        val[arr[i]] = i
    for i in range(len(arr)):
        new_target = target - arr[i]
        if new_target in val:
            return [i,val[new_target]]

print(two_sum([1,2,3,4,5],7))