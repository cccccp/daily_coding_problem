def longestpalindrome(char): # O(n^2) time complexity/ O(1) space complexity
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

# There also exists a linear time advanced algorithm due to Manacher (https://en.wikipedia.org/wiki/Longest_palindromic_substring)