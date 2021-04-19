s = str(input())
n = int(input("upto where we have to repeate this string : "))
while len(s) <= n:
    s += s
ans = s[:n].count("a")
print(ans)