# If the number of repetitions is k=2, xor can be used. The general case follows when one notes that the xor operation is just the mod 2 bitwise addition.
# It is then sufficient to perform the mod k digitwise addition in the general case. 

def lonesome(A,k=3): #O(n) time complexity/ O(1) space complexity if the entries of A are bounded
    l=0
    for a in A:
        l=max(l,int(log(a,k))+1)
   
    digits=[0]*l
    for a in A:
        q=a
        for i in range(l):
            r=q%k
            q=q//k
            digits[i]=(digits[i]+r)%k
       
    return sum(digits[i]*k**i for i in range(l))
