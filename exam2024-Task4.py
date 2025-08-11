import random
import numpy as np

def optimal_production(quan, s, y, c):  # a function which simulates the demand of the product in 30 days
    demands = []
    for day in range(s):
        demand = np.random.poisson(y)  # user input decides the average daily demand (refers to line 49)
        if demand <= quan:
            profit = (demand * 15) - (quan * c)
        else:
            profit = (quan * 15) - (quan * c) - ((demand - quan) * 10)
        demands.append(profit)

    return np.mean(demands)

np.random.seed(42)
y = 800
s = 1000
p = range(400, 1201)

## With cost = $4
avgProfits = []
for quan in p:
    profit = optimal_production(quan, s, y, c = 4)
    avgProfits.append(profit)

optimal = max(avgProfits)
optimal_ind = avgProfits.index(optimal)
optimal_quan = p[optimal_ind]

print(f"Optimal production with cost $4: {optimal_quan} units")
print(f"Average profit: ${optimal:,.2f}\n")


## With cost = $5
avgProfits = []
for quan in p:
    profit = optimal_production(quan, s, y, c = 5)
    avgProfits.append(profit)

optimal = max(avgProfits)
optimal_ind = avgProfits.index(optimal)
optimal_quan = p[optimal_ind]

print(f"Optimal production with cost $5: {optimal_quan} units")
print(f"Average profit: ${optimal:,.2f}")