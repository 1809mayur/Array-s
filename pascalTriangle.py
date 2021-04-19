def solve(A):
    matrix = []
    for i in range(A):

        a = []
        for j in range(0,i+1):
            if j == 0 or j == i:
                a.append(1)
            else:
                elems = sum(matrix[i-1][j-1:j+1])
                a.append(elems)
        matrix.append(a)
    return matrix
A = 5
print(solve(A))