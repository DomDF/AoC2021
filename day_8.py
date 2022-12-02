import os, pandas as pd, numpy as np

os.chdir(path = "/Users/ddifrancesco/Github/AoC2021")
os.listdir()

with open("day_8.txt") as file:
    data = file.readlines()

data_formatted = [data[i].strip("\n") for i in range(len(data))]

true_wiring = {"abcefg": 0, "cf":1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}
num_from_seq_length = {"2": 1, "3": 7, "4": 4, "7": 8}

def get_number_from_seq_length(seq):
    if len(seq) in [int(list(num_from_seq_length.keys())[i]) for i in range(len(num_from_seq_length.keys()))]:
        number = num_from_seq_length.get(str(len(seq)))
    else:
        number = np.nan
    return(number)


# Part 1: How many times do 1, 4, 7, or 8 appear?

nums_after_length_check = []
for i in range(len(data_formatted)):
    signals, outputs = data_formatted[i].split("|")
    outputs = [outputs.split(" ")[1:][j] for j in range(len(outputs.split(" ")[1:]))]
    nums_after_length_check.append([get_number_from_seq_length(outputs[k]) for k in range(len(outputs))])

count = 0
for i in range(len(nums_after_length_check)):
    count += len([j for j in nums_after_length_check[i] if np.isnan(j) == False])

count

# Part 2: Sum all of the full decoded sequences

def convert_wires(input_seq, output_seq):
    nums = [get_number_from_seq_length(input_seq[i]) for i in range(len(input_seq))]

    one = input_seq[np.where(np.array(nums) == 1)[0][0]]
    four = input_seq[np.where(np.array(nums) == 4)[0][0]]
    seven = input_seq[np.where(np.array(nums) == 7)[0][0]]
    eight = input_seq[np.where(np.array(nums) == 8)[0][0]]

    len_6 = np.array(input_seq)[[len(input_seq[i]) == 6 for i in range(len(input_seq))]]
    len_5 = np.array(input_seq)[[len(input_seq[i]) == 5 for i in range(len(input_seq))]]

    for num in len_6:
        if False in [signals in str(num) for signals in one]:
            six = num
        elif False in [signals in str(num) for signals in four]:
            zero = num
        else:
            nine = num

    for num in len_5:
        if False not in [signals in str(num) for signals in one]:
            three = num
        elif np.sum(np.array([signals in str(num) for signals in six])) == 5:
            five = num
        else:
            two = num

    incl_dict = {"a": np.array([zero, two, three, five, six, seven, eight, nine]),
                 "b": np.array([zero, four, five, six, eight, nine]),
                 "c": np.array([zero, one, two, three, four, seven, eight, nine]),
                 "d": np.array([two, three, four, five, six, eight, nine]),
                 "e": np.array([zero, two, six, eight]), 
                 "f": np.array([zero, one, three, four, five, six, seven, eight, nine]),
                 "g": np.array([zero, two, three, five, six, eight, nine])}

    missing_dict = {"a": np.array([one, four]),
                    "b": np.array([one, two, three, seven]),
                    "c": np.array([five, six]),
                    "d": np.array([zero, one, seven]),
                    "e": np.array([one, three, four, five, seven, nine]),
                    "f": np.array([two]),
                    "g": np.array([one, four, seven])}

    code_dict = dict()
    for letter in np.unique(np.array([i for i in "".join(i for i in true_wiring.keys())])):
        for wire in np.unique(np.array([i for i in "".join(i for i in true_wiring.keys())])):
            if (False not in [letter in incl_dict[wire][i] for i in range(len(incl_dict[wire]))]
            and True not in [letter in missing_dict[wire][i] for i in range(len(missing_dict[wire]))]):
               code_dict[letter] = wire; break

    converted_signals = []; converted_outputs = []
    for num in input_seq:
        converted_signals.append("".join(sorted([code_dict[num[j]] for j in range(len(num))])))
    for num in output_seq:
        converted_outputs.append("".join(sorted([code_dict[num[j]] for j in range(len(num))])))    

    return(converted_signals, converted_outputs)

def find_nums(converted_wires):
    return [true_wiring.get(i) for i in converted_wires]

signals_formatted = np.empty(shape = [10]); outputs_formatted = np.empty(shape = [4])
for i in range(len(data_formatted)):
    signals, outputs = data_formatted[i].split("|")
    
    np_signal = np.array(["".join(sorted(signals.split(" ")[:-1][j])) for j in range(len(signals.split(" ")[:-1]))])
    signals_formatted = np.vstack([signals_formatted, np_signal])

    np_output = np.array(["".join(sorted(outputs.split(" ")[1:][j])) for j in range(len(outputs.split(" ")[1:]))])
    outputs_formatted = np.vstack([outputs_formatted, np_output])

signals_formatted = signals_formatted[1:]; outputs_formatted = outputs_formatted[1:]

signal_nums = []; output_nums = []
for i in range(len(data_formatted)):
    converted_signals, converted_outputs = convert_wires(signals_formatted[i], outputs_formatted[i])
    
    signal_nums.append(int("".join(map(str, find_nums(converted_signals)))))       
    output_nums.append(int("".join(map(str, find_nums(converted_outputs)))))

np.sum(np.array(output_nums))