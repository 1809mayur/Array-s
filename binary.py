def bSearch(arr,v):
    mid = (0+len(arr))//2
    if arr[mid] == v:
        return mid
    elif arr[mid] < v:
        return(bSearch(arr[mid:],v))
    else:
        return(bSearch(arr[0:mid],v))

if __name__ == "__main__":
    arr = [1,2,3,4,5,11,23,44,56,66]
    v = 44
    print(bSearch(arr,v))