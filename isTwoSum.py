n = int(input())   # length of array
arr = list(map(int,input().rstrip().split()))
target = int(input())            # val which we want to find


for i in range(len(arr)):
    try:
        new_target = target - arr[i]
        if new_target in arr[i+1:]:
            print("true")
            break
    except:
        print("False")
print("false")