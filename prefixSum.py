# normal way(naive approach)
from itertools import accumulate
class PrefixSum:

    def PreSum(self,arr):
        SumList = []
        for i in range(len(arr)):
                Sum = sum(arr[:i+1])
                SumList.append(Sum)
        print(arr)
        return SumList


ar = [1,2,3,4,5]
p1 = PrefixSum()

print(p1.PreSum(ar))

### From accumulate inbuilt function of itertools module in python
print(list(accumulate(ar)))