def maxprofit(S): # O(n) time complexity/ O(1) space complexity
	n=len(S)
	
	profit=0
	maxfuture=float('-inf')
	for itin range(n-1,-1,-1):
		maxfuture=max(maxfuture,S[t])
		profit=max(profit,maxfuture-S[t])
	
	return profit
