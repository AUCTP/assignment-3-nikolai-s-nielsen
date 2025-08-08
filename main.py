# My code

import random
import numpy as np

### Task 1 ###

## Simulation of 30 days ##  # this code is locked to not run simultaneously with the solution of Task 2 
# def simulate_demand1(n):
#     demands = []
#     for day in range(n):
#         demand = np.random.poisson(20)
#         demands.append(demand)

#     return demands

# n = 30
# demandToday = simulate_demand1(n)

# demandTotal = sum(demandToday)
# print(f'The total demand is: {demandTotal}')

# avg = round(np.average(demandToday),2)
# print(f'The average demand is: {avg}')

# std = round(np.std(demandToday),2)
# print(f'The standard deviation of demand is: {std}')

# percentileLow = round(np.percentile(demandToday, 5),2)
# print(f'The 5th percentile of demand is: {percentileLow}')

# percentileHigh = round(np.percentile(demandToday, 95),2)
# print(f'The 95th percentile of demand is: {percentileHigh}')
# print(f'\n')


### Task 2 ###

## A 1000 simulations of 30 days ##
def simulate_demand2(n, y):  # a function which simulates the demand of the product in 30 days
    demands = []
    for day in range(n):
        demand = np.random.poisson(y)  # user input decides the average daily demand (refers to line 49)
        demands.append(demand)

    return demands  # returns a list of the daily demands in 30 days

def simulate_optimal_inventory():  # a function which takes user input to calculate and describe the optimal inventory level of the product
    print("Welcome!")
    while True:
        choice = input('Press 1 to simulate optimal inventory level for one month\nPress 2 to terminate\n>')
        if choice == "1":    
            y = int(input('Choose an average daily demand (e.g. 20): '))
            serviceLevel = float(input('Choose a service level between 0 and 100 (e.g. 95): '))
            x = 100000  # the function is set to run the average demand in 30 days a 1000 times 
            
            demandTotal = []

            for number in range(x):    
                n = 30
                demandToday = simulate_demand2(n, y)
                demandTotal.append(sum(demandToday))

            print('\nSummary of statistics:')
            demandSum = round(np.mean(demandTotal),0)
            print(f'\tThe total demand is: {demandSum}')

            std = round(np.std(demandTotal),2)
            print(f'\tThe standard deviation of demand is: {std}')

            percentileLow = round(np.percentile(demandTotal, 5),2)
            print(f'\tThe 5th percentile of demand is: {percentileLow}')

            percentileHigh = round(np.percentile(demandTotal, 95),2)
            print(f'\tThe 95th percentile of demand is: {percentileHigh}')

            inventoryOptimal = round(np.percentile(demandTotal, serviceLevel))
            print(f'\nThe optimal inventory level with an average daily demand of {y} and service level of {serviceLevel} is: {inventoryOptimal}\n')
        else:
            print("Goodbye!")
            break

simulate_optimal_inventory()


# Interpretation
    # The function describes that by having an average daily demand of 20 and a service level of 95%
    # the total demand in 30 days will be 600 items and an optimal inventory level of 641 items