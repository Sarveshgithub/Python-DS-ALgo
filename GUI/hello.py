import os
import sys
import SudoKu
SudoKu.main()
from tkinter import *

root = Tk()
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]
# create 9x9 grid
for i in range(0, 9):
    for j in range(0, 9):
        if board[i][j] == 0:
            Entry(root, width=5, borderwidth=0).grid(row=i, column=j)
        else:
            Button(root, text=str(board[i][j]), width=5, borderwidth=0).grid(row=i, column=j)
        # print(board[i][j])
        # Button(root, text=str(i * j)).grid(row=i, column=j)
root.mainloop()
