
def dynamicArray(n, queries):
    # Write your code here
    arr = []
    for i in range(n):
        arr.append([])         # n size nested array created.
    last_answer  = 0
    for i in queries:
        q = int(i[0])
        x = int(i[1])
        y = int(i[2])
        if q == 1:
            idx = ((x ^ last_answer)% n)
            arr[idx].append(y)
        if q == 2:
            idx = ((x ^ last_answer)% n)
            last_answer = arr[idx].pop()
            print(last_answer)
    return 0


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    print(result)
