def arbitrage(currencies): #O(n^2) optimal solution
	n=len(currencies[0])
	return not(all(all(currencies[0][j]==currencies[0][i]*currencies[i][j] and currencies[i][j]!=0 for i in range(n)) for j in range(n)))
