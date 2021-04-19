for i in range(1,10):
    print(i >> 1,end = " ")
    print(i//2)              #instead of diving by 2 Do right shift.
                             #Do left shift insted of multiple of 2.
        
def iseven(n):
    if n & 1 == 0 :
        return True
    else:
        return False

print(iseven(100000000000000000000000000000000000000000000000000000000000000001123279888))

def Swap(a,b):
    temp = a 
    a = b
    b = temp
    return "{},{}".format(a,b)

print(Swap(20,300))
# by bit operator.
def swap(a,b):
    a = a^b
    b = a^b
    a = a^b
    return "{},{}".format(a,b)
print(swap(212,21))
