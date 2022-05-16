import os, requests, numpy as np

os.chdir(path = "/Users/ddifrancesco/OneDrive - The Alan Turing Institute/AoC")
os.listdir()

with open("day_4.txt") as file:
    data = file.readlines()

# Part 1: Find the score (sum of unmarked numbers multiplied by final number called)
# of the winning bingo board

calls = data[0].split(",")

i = int(0); skip = 5; indices = []
for i in np.arange(start = 2, stop = len(data), step = skip + 1):
    indices.append(list(np.arange(start = i, stop = i + skip, step = 1)))
    i = i + skip + 1

def get_board_matrix(board_list):
    return(np.asmatrix([np.array(x.replace("\n", "").split()) for x in board_list]))

n_boards = len(indices)

from operator import itemgetter

boards = []
for i in np.arange(start = 0, stop = n_boards, step = 1):
    boards.append(get_board_matrix(itemgetter(*indices[i])(data)))

class bingo_board:
    def __init__(self, board_matrix):
        self.matrix = board_matrix
        self.nrows = self.matrix.shape[1]
        self.ncols = self.matrix.shape[0]

    def play_bingo(self, bingo_calls):
        verif_matrix = np.zeros(shape = self.matrix.shape)

        for call_id, call in enumerate(bingo_calls):
            match_id = np.where(self.matrix == call)

            if len(match_id[0]) > 0:
                verif_matrix[match_id] = 1

            row_score = np.sum(verif_matrix, axis = 0).max()
            col_score = np.sum(verif_matrix, axis = 1).max()

            if row_score == self.ncols or col_score == self.nrows:
                results = verif_matrix, call_id; break
            else:
                results = "Not a winning board"

        return(results)

draws_to_win = []
for board in boards:
    draws_to_win.append(bingo_board(board_matrix = board).play_bingo(bingo_calls = calls)[1])

winning_board_id = np.where(np.asarray(draws_to_win) == np.asarray(draws_to_win).min())[0][0]

winning_board = bingo_board(board_matrix = boards[winning_board_id])

winning_board_results = winning_board.play_bingo(bingo_calls = calls)

winning_final_call = calls[winning_board_results[1]]

winning_unmarked_numbers = winning_board.matrix[np.where(winning_board_results[0] == 0)]

winning_board_score = int(winning_final_call) * np.sum(winning_unmarked_numbers.astype(int))

# Part 2: Which board will win last and what is it's score?

losing_board_id = np.where(np.asarray(draws_to_win) == np.asarray(draws_to_win).max())[0][0]

losing_board = bingo_board(board_matrix = boards[losing_board_id])

losing_board_results = losing_board.play_bingo(bingo_calls = calls)

losing_final_call = calls[losing_board_results[1]]

losing_unmarked_numbers = losing_board.matrix[np.where(losing_board_results[0] == 0)]

losing_board_score = int(losing_final_call) * np.sum(losing_unmarked_numbers.astype(int))
