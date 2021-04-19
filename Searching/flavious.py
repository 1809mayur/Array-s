def flavius(n):

    L = list(range(1, n+1)); 
    j=2
    while j <= len(L):

        L = [L[i] for i in range(len(L)) if (i+1)%j]

        j+=1

    if n in L:
        return "Yes"
    else:
        return "No"

print(flavius(17))