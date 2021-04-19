count =0
def length(arr):
    global count
    if len(arr) == 1:
        return len(arr)+count
    if arr[0] == 0:
        count = count + 1
        arr.remove(arr[0])
    else:
        arr[0:2] = [arr[0]%arr[1]]


    return length(arr)
print(length([4,2,3,1,0]))