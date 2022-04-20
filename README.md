# Algo Project
## Log Parser (logparse.py)

Accepts a filename on the command line. The file is a Linux-like log file from a system you are debugging. Mixed in among the various statements are messages indicating the state of the device. They look like this:

The device state message has many possible values, but this program cares about only three: ON, OFF, and ERR.

Your program will parse the given log file and print out a report giving how long the device was ON and the timestamp of any ERR conditions.


## Sudoku Solver (sudokusolve.py)

Given a string in SDM format, described below, write a program to find and return the solution for the sudoku puzzle in the string. The solution should be returned in the same SDM format as the input.

Some puzzles will not be solvable. In that case, return the string “Unsolvable”.

For our purposes, each SDM string will be a sequence of 81 digits, one for each position on the sudoku puzzle. Known numbers will be given, and unknown positions will have a zero value.


## Keypad_string
    
Given a string consisting of 0-9, find the string that is created using a standard phone keypad
You can ignore 1, and 0 corresponds to space.
