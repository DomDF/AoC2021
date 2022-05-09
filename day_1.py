import os, pandas as pd, numpy as np

os.chdir(path = "/Users/ddifrancesco/OneDrive - The Alan Turing Institute/AoC")
os.listdir()

seabed_meas = pd.read_csv(filepath_or_buffer = 'day_1_data.csv', header = None, squeeze = True)

seabed_meas.head(n = 3)

count = 0; interval = 3; d_depth = np.array([np.nan])

for i in range(1, len(seabed_meas)):
    diff = (seabed_meas - seabed_meas.shift(periods = interval, fill_value = np.nan))[i]
    if (diff > 0):
        d_depth = np.append(d_depth, [1]); count += 1
    elif (diff < 0):
        d_depth = np.append(d_depth, [-1])
    else:
        d_depth = np.append(d_depth, [0])

count

np.unique(d_depth, return_index = True, return_counts = True, axis = 0)

df = pd.concat((seabed_meas, pd.Series(d_depth)), axis = 1)
df.columns = ["Measurement", "Direction"]

dir_counts = df.Direction.value_counts(dropna = False)

dir_counts

len(df[df.Direction == 1])
