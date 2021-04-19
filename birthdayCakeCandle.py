n = int(input())
candles = list(map(int,input().rstrip().split()))
candles.sort(reverse = True)
count = 0
i = 0
while candles[i] == candles[i+1]:
    count = count + 1
    i = i+1

print(count)