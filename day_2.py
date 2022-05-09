import os, pandas as pd, numpy as np

os.chdir(path = "/Users/ddifrancesco/OneDrive - The Alan Turing Institute/AoC")
os.listdir()

directions = pd.read_csv(filepath_or_buffer = 'day_2_data.csv', header = None, squeeze = True)

directions.head(n = 3)

directions[0]

import re

# Checking all possible directions in data
dirs = np.array(np.nan); mags = np.array(np.nan)
for d in directions:
    dirs = np.append(dirs, d.split()[0])
    mags = np.append(mags, d.split()[1])

np.unique(dirs)
np.unique(mags)

dir_df = pd.DataFrame.from_dict(data = {"Iteration" : [0], "aim" : [0], "x" : [0], "y" : [0]})

dir_df

for i in range(len(directions)):
    d = directions[i]
    if(re.search(pattern = "up", string = d)):
        dir_dict = {"Iteration" : [dir_df.Iteration.values[i] + 1], "aim" : [dir_df.aim.values[i] - int(d[-1])],
                    "x" : [dir_df.x.values[i]], "y" : [dir_df.y.values[i]]}
    elif(re.search(pattern = "down", string = d)):
        dir_dict = {"Iteration" : [dir_df.Iteration.values[i] + 1], "aim" : [dir_df.aim.values[i] + int(d[-1])],
                    "x" : [dir_df.x.values[i]], "y" : [dir_df.y.values[i]]}
    elif(re.search(pattern = "forward", string = d)):
        dir_dict = {"Iteration" : [dir_df.Iteration.values[i] + 1], "aim" : [dir_df.aim.values[i]],
                    "x" : [dir_df.x.values[i] + int(d[-1])], "y" : [dir_df.y.values[i] + int(d[-1]) * dir_df.aim.values[i]]}
    dir_df = pd.concat(objs = [dir_df, pd.DataFrame.from_dict(data = dir_dict)])

directions.tail(n = 3)
dir_df.tail(n = 3)

from plotnine import *

point_df = pd.DataFrame.from_dict(data = {"x" : [dir_df.x.values[-1]], "y" : [dir_df.y.values[-1]],
                                          "label" : f"x = {dir_df.x.values[-1]}, \ny = {dir_df.y.values[-1]}, \naim = {dir_df.aim.values[-1]}"})

(ggplot(data = dir_df, mapping = aes(x = "x", y = "y"))+
geom_path(mapping = aes(color = "aim"), alpha = 1/2)+
geom_point(data = point_df, mapping = aes(x = "x", y = "y"),
           size = 3, alpha = 1/2)+
geom_text(data = point_df, mapping = aes(x = point_df.x - 300, y = "y", label = "label"))+
scale_x_continuous(name = "Horizontal distance", limits = [0, 2000])+
scale_y_continuous(name = "Depth", limits = [0, 11*10**5])+
theme_matplotlib())

point_df.x.values * point_df.y.values
