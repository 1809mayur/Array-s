A = [ 28, 68, 100, 90, 46, 58, 54, 74 ]
B = 78
count = 0
for i in range(B):
    count = count +1
    A.insert(0,A[-1])
    A.pop()
    

print(A)
# A.insert(0)
# print(A)