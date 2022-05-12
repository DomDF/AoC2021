import os, requests, pandas as pd, numpy as np

os.chdir(path = "/Users/ddifrancesco/OneDrive - The Alan Turing Institute/AoC")
os.listdir()

# Part 1: Find the number of locations where at least 2 lines overlap

with open("day_5.txt") as file:
    data = file.readlines()

x_start = np.asarray([int(x.split()[0].split(",")[0]) for x in data])
y_start = np.asarray([int(x.split()[0].split(",")[1]) for x in data])

x_end = np.asarray([int(x.split()[2].split(",")[0]) for x in data])
y_end = np.asarray([int(x.split()[2].split(",")[1]) for x in data])

def get_path(begin, end):
    if abs(begin - end) > 0:
        result = np.linspace(start = begin, stop = end, num = abs(end - begin) + 1, dtype = int)
    else:
        result = np.array(begin).reshape(-1)
    return(result)

x_coords = []; y_coords = []; vh_line = []
for i in range(len(data)):
    dx = get_path(begin = x_start[i], end = x_end[i]); dy = get_path(begin = y_start[i], end = y_end[i])
    x_coords.append(dx); y_coords.append(dy)
    if len(dx) == 1 or len(dy) == 1:
        vh_line.append(1)
    else:
        vh_line.append(0)

vh_x_coords = np.asarray(x_coords)[np.where(np.asarray(vh_line) == 1)]
vh_y_coords = np.asarray(y_coords)[np.where(np.asarray(vh_line) == 1)]

num_vl_lines = len(np.asarray(vh_line)[np.where(np.asarray(vh_line) == 1)])
vh_tracking_matrix = np.zeros(shape = (1000, 1000))
for i in range(num_vl_lines):
    vh_tracking_matrix[vh_x_coords[i], vh_y_coords[i]] += 1

vh_indices = np.where(vh_tracking_matrix >= 2)
vh_tracking_matrix[vh_indices].shape

# Part 2: Also considering diagonal lines

tracking_matrix = np.zeros(shape = (1000, 1000))
for i in range(len(data)):
    tracking_matrix[x_coords[i], y_coords[i]] += 1

indices = np.where(tracking_matrix >= 2)
tracking_matrix[indices].shape
