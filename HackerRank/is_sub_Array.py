s1 = input()
s2 = input()

s_set = set(s1)
s2_set = set(s2)
ans = False
for i in range(len(s2)):
    if s_set.intersection(s2_set):
        ans = True
        print(True)
        break
if ans == False:
    print(False)
    
