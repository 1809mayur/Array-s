from itertools import permutations
s = str(input())
possible = ["".join(i) for i in permutations(s)]
print(possible)