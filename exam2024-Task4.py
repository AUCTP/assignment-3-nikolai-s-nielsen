import random
import numpy as np

## With cost = $4
def optimal_production(quan):  # a function which simulates the demand of the product in 30 days
    y = 800
    demands = []
    for day in range(s):
        demand = np.random.poisson(y)  # user input decides the average daily demand (refers to line 49)
        if demand <= quan:
            win = (demand * 15) - (quan * 4)
            demands.append(win)
        else:
            loss = (quan * 15) - (quan * 4) - ((demand - quan) * 10)
            demands.append(loss)

    return np.mean(demands)

s = 1000
p = range(400, 1201)
avgProfits = [optimal_production(quan) for quan in p]

optimal = max(avgProfits)
optimal_quan = p[np.argmax(avgProfits)]

print(f"Optimal production with cost $4: {optimal_quan} units")
print(f"Average profit: ${optimal:,.2f}\n")


## With cost = $5
def optimal_production(quan):  # a function which simulates the demand of the product in 30 days
    y = 800
    demands = []
    for day in range(s):
        demand = np.random.poisson(y)  # user input decides the average daily demand (refers to line 49)
        if demand <= quan:
            win = (demand * 15) - (quan * 5)
            demands.append(win)
        else:
            loss = (quan * 15) - (quan * 5) - ((demand - quan) * 10)
            demands.append(loss)

    return np.mean(demands)

s = 1000
p = range(400, 1201)
avgProfits = [optimal_production(quan) for quan in p]

optimal = max(avgProfits)
optimal_quan = p[np.argmax(avgProfits)]

print(f"Optimal production with cost $5: {optimal_quan} units")
print(f"Average profit: ${optimal:,.2f}")