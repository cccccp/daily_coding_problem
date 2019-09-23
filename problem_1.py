def sum_two(array,k): #O(n) time/space complexity (search in a set is O(1) on average)
    s=set(k-x for x in array)
    return any(x in s for x in array)

# If the numbers are supposed to be used accordingly to their counts in the array

def sum_two(array,k): #O(n) time/space complexity (search in a set is O(1) on average)
    s=set()
    
    for x in array:
        if x in s:
            return True
        s.add(k-x)  
    
    return False
