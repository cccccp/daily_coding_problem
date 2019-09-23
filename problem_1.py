def sum_two(array,k): #O(n) time/space complexity (search in a set is O(1) on average)
    s=set(k-x for x in array)
    return any(x in s for x in array)
