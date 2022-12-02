import os, pandas as pd, numpy as np

os.chdir(path = "/Users/ddifrancesco/Github/AoC2021")
os.listdir()

with open("day_7.txt") as file:
    data = file.readline()

# Part 1: Minimum number of horizontal moves to align all crab submarines

h_pos = np.array([int(i) for i in data.split()[0].split(",")])
median_h_pos = np.median(h_pos)

total_moves = np.sum(np.abs(median_h_pos - h_pos))

# Part 2: The cost of sequential moves in any direction increases.
# Find the new optimal position and total cost

def triangular_number(n):
    return sum(range(n + 1))

costs = []
for pos in range(h_pos.max()):
    distance = np.abs(pos - h_pos)
    costs.append(sum([triangular_number(n = int(i)) for i in distance]))

optimal_index = np.where(np.array(costs) == np.array(costs).min())

optimal_cost = np.array(costs)[optimal_index][0]
