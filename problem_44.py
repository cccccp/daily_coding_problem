def inversions_merge(A1,A2): # auxilary function to merge 2 sorted lists and count the number of remaining inversions (O(max(n1,n2)) time complexity, O(n1+n2) space complexity)         
    n1, n2=len(A1), len(A2) 
    A = A1 + A2
    
    inv = 0
    i, j = 0, n1          

    while j < n1+n2:
        i=0
        while A[i] < A[j]:
            i += 1
        if i < j:
            inv+=j-i
            A[i+1:j+1]=A[i:j]
            A[i]=A2[j-n1]
        elif i==j:
            j += 1
    return inv, A
    
def inversions(A): # O(nlog(n)) time/space complexity
    n=len(A)
    if n<2:
        return 0,A
    inv1, A1 = inversions(A[:n//2])
    inv2, A2 = inversions(A[n//2:])
    inv, A = inversions_merge(A1, A2) 
    return inv+inv1+inv2, A    
