def subsetsum(A,x):
    n=len(A)
    
    tab=[True]+[False]*x
    complete_tab=[tab]
    
    # determine whether x can be obtained as a sum of a subset of set(A) 
    for j in range(n):
        tab=[ tab[i] or (A[j]<=i and tab[i-A[j]]) for i in range(x+1)]
        complete_tab.append(tab)
    
    # build the subset
    if tab[-1]:
        subset=set()
        i=x
        for j in range(n-1,-1,-1):
            if complete_tab[j+1][i]!=complete_tab[j][i]:
                i-=A[j]
                subset.add(A[j])
        
        return subset
        
    else:
        return None
    
def partition(A): # a multiset is understood as a list here
    S=sum(A)
    if S%2==0:
        return subsetsum(A,S//2)
    else:
        return None
    
