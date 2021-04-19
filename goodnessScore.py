
def goodness(arr,K):
    count = 0
    minioperation = 0
    n = len(arr)
    for i in range(1,(n//2)+1):
        if arr[i] != arr[n-1-i]:
            count = count + 1
    if count == K:
        minioperations = 0
    elif count > K:
        minioperations = count - K
    else:
        minioperations = (K - count) * (-1)
    return minioperations
        
    
   
        
    



if "__main__" == __name__:
    T = int(input())
    for i in range(T):
        NK = input().rstrip().split()
        arr = str(input())
        N = (NK[0])
        K = int(NK[1])
        
        result = goodness(N,K)
        print(result)
        
    