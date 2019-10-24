def longestpalindrome(char): # Manacher's algorithm: O(n) time/space complexity
    # To avoid problems with even sized longest palindroms
    s="^#"+"#".join(char)+"#$"
    n=len(s)
    
    # definition of two auxilary parameters (right is the upper index of the previous longest palindrom; center is the corresponding position)
    cen=0
    right=0
    
    # array of the lengths of the longest palindroms centered at any position
    p=[0]*n
    
    pal=""
    length=0
    
    for i in range(1,n-1):
        
        # definition of a lower bound for the palindrom centered at i
        
        # Since (obviously) i+ min(p[mir],right-i)<=right, one has mir-min(p[mir],right-i)>=left (the symmetric of right, w.r.t. cen) 
        # and the palindrom centered in mir of radius min(p[mir],right-i) is included in the first-half of the longest palindrom centered in cen.
        # Hence p[i] >=min(p[mir],right-i) (the symmetric of any palindrom centered in mir, w.r.t. cen, is also a palindrom).
        
        mir=cen-(i-cen)
        p[i]=max(0,min(p[mir],right-i))
        
        # determination of the length of the longest palindrom centered at i
        while p[i]+1<=min(i,n-1-i) and s[i-p[i]-1]==s[i+p[i]+1]:
            p[i]+=1
        
        if p[i]>length:
            length=p[i]
            pal=s[i-p[i]:i+p[i]+1]
            
        # new definition of the auxilary indexes
        if i+p[i]>right:
            right=i+p[i]
            cen=i
    
    word_pal=[c for c in pal if c != "^" and c != "#" and c != "$"]
    pal="".join(word_pal)
    
    return pal
