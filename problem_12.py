def ways(N): #O(N) time complexity/ O(1) space complexity
    if N==1:
        return 1
    elif N==2:
        return 2
    else:
        u,v=1,2
        for _ in range(N-1):
            u,v=v,u+v
        return u
