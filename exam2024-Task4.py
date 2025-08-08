import random
import numpy as np

def optimal_production(n, y):  # a function which simulates the demand of the product in 30 days
    demands = []
    for day in range(n):
        demand = np.random.poisson(y)  # user input decides the average daily demand (refers to line 49)
        demands.append(demand)

    return demands


n = 100000
y = 800
sum = sum(optimal_production(n, y)) / n
revenue = sum * 15
cost = sum * 4
profit = revenue - cost

print(round(revenue))
print(round(cost))
print(round(profit))
print(round(sum))