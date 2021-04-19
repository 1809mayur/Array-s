def median(ar1,ar2):
    return (sum(ar1)+sum(ar2))/(len(ar1)+len(ar2))
# user input for elements of ar1.
ar1 = list(map(int,input().rstrip().split()))
#for ar2.
ar2 = list(map(int,input().rstrip().split()))

print(median(ar1,ar2))