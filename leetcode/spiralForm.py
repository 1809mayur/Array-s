def spiralOrder(A):
    ls = []
    m = len(A)
    n = len(A[0])
    T,B,R,L,D = 0,m-1,n-1,0,0
    while T <= B and L <= R:
        if D == 0:
            for i in range(T,R+1):
                ls.append(A[T][i])
            T  = T + 1
            D = 1
        elif D == 1:
            for i in range(T,B+1):
                ls.append(A[i][R])
            R = R - 1
            D = 2
        elif D == 2:
            for i in range(R,L-1,-1):
                ls.append(A[B][i])            
            B = B - 1
            D = 3
        elif D == 3:
            for i in range(B,T-1,-1):
                ls.append(A[i][L])
            L = L + 1
            D = 0
    return ls
A = [[1,2,3,4],[4,5,6,56],[7,8,9,90],[3,7,9,0 ]]
print(type(A))
print(spiralOrder(A))