import os, pandas as pd, numpy as np

os.chdir(path = "/Users/ddifrancesco/OneDrive - The Alan Turing Institute/AoC")
os.listdir()

binary_codes = pd.read_excel(io = 'day_3_data.xlsx', header = None, squeeze = True, dtype = str)
binary_codes.head()

lengths = np.array(np.nan)
for i in range(len(binary_codes)):
    c = binary_codes[i]
    lengths = np.append(lengths, np.array(len(c)))
# All binary codes are 12 digits long
np.unique(lengths)

n_rows = len(binary_codes); n_cols = len(binary_codes[0])

digits = np.array([int(i) for i in binary_codes[0]])
digits

for i in range(1, len(binary_codes)):
    digits = np.vstack((digits, [int(j) for j in binary_codes[i]]))

γ_binary = np.array([]); ϵ_binary = np.array([])

import collections

for d in range(digits.shape[1]):
    γ_binary = np.append(γ_binary, int(collections.Counter(digits[:,d]).most_common()[0][0]))
    ϵ_binary = np.append(ϵ_binary, int(collections.Counter(digits[:,d]).most_common()[1][0]))

ϵ_binary
γ_binary

def translate_binary(binary_array):
    sum = 0
    for i in range(len(binary_array)):
        index = (len(binary_array) - i) - 1 # Index reverses the order of i, and starts at zero
        sum = sum + binary_array[i] * 2 ** index
    return(sum)

γ_rate = translate_binary(binary_array = γ_binary)
ϵ_rate = translate_binary(binary_array = ϵ_binary)

power_consumption = γ_rate * ϵ_rate
power_consumption

def get_target(bit_criteria, param):
    target = int()
    count = [x[1] for x in collections.Counter(bit_criteria).most_common()]
    if len(count) > 1:
        if count[0] == count[1]:
            target = 1
        else:
            target = collections.Counter(bit_criteria).most_common()[0][0]
    if param == "CO2":
        return abs(target-1)
    else:
        return target

def filter_bit_criteria(bit_criteria, index, target):
    if len(bit_criteria[bit_criteria[:, index] == target]) >= 1:
        bit_criteria = bit_criteria[bit_criteria[:, index] == target]
    else:
        bit_criteria = bit_criteria
    return bit_criteria

CO2_bit_criteria = digits; O2_bit_criteria = digits
for l in range(digits.shape[1]):
    CO2_target = get_target(bit_criteria = CO2_bit_criteria[:, l], param = "CO2")
    CO2_bit_criteria = filter_bit_criteria(bit_criteria = CO2_bit_criteria, index = l, target = CO2_target)

    O2_target = get_target(bit_criteria = O2_bit_criteria[:, l], param = "O2")
    O2_bit_criteria = filter_bit_criteria(bit_criteria = O2_bit_criteria, index = l, target = O2_target)

CO2_bit_criteria[0]
O2_bit_criteria[0]

CO2_scrubber_rating = translate_binary(binary_array = CO2_bit_criteria[0])
O2_generator_rating = translate_binary(binary_array = O2_bit_criteria[0])

life_support_rating = CO2_scrubber_rating * O2_generator_rating
life_support_rating
