import os, pandas as pd, numpy as np

os.chdir(path = "/Users/ddifrancesco/OneDrive - The Alan Turing Institute/AoC")
os.listdir()

with open("day_6.txt") as file:
    data = file.readline()

from collections import Counter

day_zero_fish = Counter([int(i) for i in data.split()[0].split(",")])

# Part 1: How many fish will there be after 80 days

def get_number_laternfish(current_states, n_days):
    fish = dict(current_states)
    for day in range(n_days):
        fish_list = [fish.get(i, 0) for i in range(9)]
        n_new_fish = fish_list[0]
        new_pop_list = fish_list[1:]
        new_pop_list.append(n_new_fish)
        new_pop_list[6] += n_new_fish
        fish = dict(zip([i for i in range(9)], new_pop_list))
        total_fish = sum([fish.get(i, 0) for i in range(9)])
    return(fish, total_fish)

total_days = 80
get_number_laternfish(current_states = day_zero_fish, n_days = total_days)[1]

# Part 2: How many fish after 256 days?

total_days = 256
get_number_laternfish(current_states = day_zero_fish, n_days = total_days)[1]
