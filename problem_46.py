def longestpalindrome(char):
    n=len(char)
    l=0
    pal=''
    for c in range(n):
        i=0
        while c-i >=0 and c+i<n and char[c-i]==char[c+i]:
            if 2*i+1>l:
                l=2*i+1
                pal=char[c-i:c+i+1]
            i+=1
    return pal    
