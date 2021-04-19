def utopianTree(n):
    val = 0
    for i in range(n+1):
        if i % 2 == 0:
            val = val + 1
        else:
            val = val * 2
    return val
        

n = int(input())
for i in range(n):
    result = utopianTree(int(input("cycle:")))
    print(result)

    