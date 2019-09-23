# Optional use of float('inf') if the costs are integer (one can use INT_MAX instead)

def minimum_cost(costs):
    N=len(costs)
    K=len(costs[0])
    
    cost=min(costs[0])
    color=costs[0].index(cost)
    
    i=-1
    current_cost=float('inf')
    for n in range(1,N): 
        for k in range(K):
            if k!=color:
                if costs[n][k]<current_cost:
                    i,current_cost=k,costs[n][k]
        color=i
        cost+=current_cost
        
    return cost  
