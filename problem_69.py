def maxproduct3(l):
    l.sort()
    return max(l[-1]*l[-2]*l[-3],l[0]*l[1]*l[-1])
# One can also avoid to sort the list (it is sufficient to get the two smallest values of l along with its three largest).
