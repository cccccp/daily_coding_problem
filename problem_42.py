def sumsto(l,K):# Dynamic programming approach in O(n*K) space/time complexity
    n=len(l)
    
    # At each step, we build an array of booleans of the values<=K that can be obtained using only the first i elements of the list l 
    aux=[True]+[False]*K
    tab=[aux]
    for i in range(n):
        aux=[aux[k] or aux[k-l[i]] for k in range(K+1)]
        tab.append(aux)
    
    # We now recover the list of elements which sum to K 
    # /!\ Line i of tab corresponds to the values that can be obtained by using the elements of list l of index <=i-1
    if tab[-1][-1]:
        elements=[]
        k=K
        for i in range(n,-1,-1):
            if tab[i][k] and not(tab[i-1][k]):
                elements.append(l[i-1])
                k-=l[i-1]
                print(l[i-1])
        return elements
    else:
        return None
