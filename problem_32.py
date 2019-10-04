def arbitrage(currencies):
	n=len(currencies[0])
	return not(all(all(currencies[0][j]==currencies[0][i]*currencies[i][j] for i in range(n)) for j in range(n)))
  
