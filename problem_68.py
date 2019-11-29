def attacks(bishops):
    n=len(bishops)
    attacksnumber=0
    for i in range(n):
        for j in range(i):
            b1=bishops[i]
            b2=bishops[j]
            if abs(b1[0]-b2[0])==abs(b1[1]-b2[1]):
                attacksnumber+=1
    return attacksnumber
