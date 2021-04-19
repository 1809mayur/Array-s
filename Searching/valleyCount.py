steps = int(input())
path = str(input())
def countingValleys(steps, path):
    # Write your code here
    lowerCount = 0

    upperCount = 0
    valley = 0
    i = 0
    while i < steps:
        pos = i
        if path[i] == "U":
            upperCount += 1
        else:
            lowerCount += 1

        if upperCount - lowerCount < 0:
            j = i
            while j < steps:
                if upperCount - lowerCount == 0:
                    valley += 1
                    upperCount = 0
                    lowerCount = 0
                    j += 1
                    pos = j
                j += 1
        i = pos
    return valley

print(countingValleys(steps,path))
