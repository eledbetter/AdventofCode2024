'''
Day 2 Part 1

https://adventofcode.com/2024/day/2
'''

# 1. open input file
from pathlib import Path

path = Path(__file__).resolve().parent.parent / 'inputs' / 'day_02.txt'
inp = open(path)

# 2. loop thru each line
#       - convert line to list of int
safeCount = 0
for line in inp:
    ls = [int(x) for x in line.split()]
    
    # 3. loop thru each list element
    #       - increment safeCount if all levels in list are safe:
    #               - levels are either all increasing or all decreasing
    #               - any two adjacent levels differ by at least one and at most three
    diff = 0
    isSafe = 1
    for i in range(1, len(ls)):
        # check if distance too great
        if abs(ls[i - 1] - ls[i]) > 3:
            isSafe = 0
            break
        # check if direction changed
        elif i > 1 and diff * (ls[i - 1] - ls[i]) < 1:
            isSafe = 0
            break
        diff = ls[i - 1] - ls[i]
    
    safeCount += isSafe

inp.close()

# 4. output solution
print(safeCount)