'''
Day 2 Part 2

https://adventofcode.com/2024/day/2
'''

def findUnsafeIndex(inpLs):
    '''Returns index of first unsafe level.
    If there are no unsafe levels, returns -1.

    A list is safe if the following are true:
        - levels are either all increasing or all decreasing
        - any two adjacent levels differ by at least one and at most three
    '''
    if inpLs == None:
        return 999
    
    unsafeIndex = -1
    diff = 0
    for i in range(0, len(inpLs) - 1):
        # check if distance too great
        if (abs(inpLs[i] - inpLs[i+1]) > 3):
            unsafeIndex = i
            break
        # check if direction changed
        elif i > 0 and diff * (inpLs[i] - inpLs[i+1]) < 1:
            unsafeIndex = i
            break
        diff = inpLs[i] - inpLs[i+1]
    return unsafeIndex


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
    #               - if removing 1 level makes list safe, then it is counted as safe

    isSafe = 1
    unsafeIndex = findUnsafeIndex(ls)

    # if one level is unsafe, then check if removing that level, the level before, or the level after would make it safe
    if unsafeIndex > -1:
        slice1 = ls.copy()
        slice2 = ls.copy()
        slice3 = ls.copy()
        if unsafeIndex == 0:
            slice1 = None
            slice2.pop(unsafeIndex)
            slice3.pop(unsafeIndex+1)
        elif unsafeIndex == len(ls) - 1:
            slice1.pop(unsafeIndex-1)
            slice2.pop(unsafeIndex)
            slice3 = None
        else:
            slice1.pop(unsafeIndex-1)
            slice2.pop(unsafeIndex)
            slice3.pop(unsafeIndex+1)
        
        # checking if removing any levels around problematic index creates a safe list
        if (findUnsafeIndex(slice1) != -1) and (findUnsafeIndex(slice2) != -1) and (findUnsafeIndex(slice3) != -1):
            isSafe = 0

    safeCount += isSafe

inp.close()

# 4. output solution
print(safeCount)