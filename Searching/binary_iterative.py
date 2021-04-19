
arr = [1,2,3,4,5,6,7,12,34]
val = 55
low = 0
high = len(arr)
mid = (low+high)//2

while low < high:

    if arr[mid] == val:
        print("position is",mid)
        break
    elif arr[mid] < val:
        low = mid
        mid = (low + high)//2
    else:
        high = mid
        mid =(low+high)//2
    low += 1
print("absent")




