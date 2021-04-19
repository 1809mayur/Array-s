

ar = [[1,2,3],[4,5,6],[7,8,9]]
m = 3
ls = []
n = 3
top,bottom = 0,m-1
left,right = 0,n-1
count = 0
while top <= bottom and left <= right:
    if count == 0:
        for i in range(left,right+1):
            ls.append(ar[top][i])
        top += 1
        count += 1
    elif count == 1 :
        for i in range(top,bottom+1):
            ls.append(ar[i][right])
        right -= 1
        count += 1
    elif count == 2:
        for i in range(right,left-1,-1):
            ls.append(ar[bottom][i])
        bottom -= 1
        count += 1
    else:
        for i in range(bottom,top-1,-1):
            ls.append(ar[i][left])
        left += 1
        count = 0
print(ls)

