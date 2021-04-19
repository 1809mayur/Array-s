def fizzBuzz(A):
    ans = [i for i in range(1,A+1)]
    for i in range(2,A,3):
        ans[i] = "Fizz"
    for i in range(4,A,5):
        ans[i] = "Buzz"
    for i in range(14,A,15):
        ans[i] = "FizzBuzz"
    return ans
print(fizzBuzz(30))