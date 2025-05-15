'''
Day 1 Part 2

https://adventofcode.com/2024/day/1
'''

# 1. open input file
from pathlib import Path

path = Path(__file__).resolve().parent.parent / 'inputs' / 'day_01.txt'
inp = open(path)

# 2. extract numbers from file
#       - loop thru each line
#       - first num is added to hashmap as value
#       - second num is added to list

hashmap = {}
rightList = []

for line in inp:
    split = line.split()
    hashmap[int(split[0])] = 0
    rightList.append(int(split[1]))

inp.close()

# 3. calc similarity score
#       - loop thru list
#       - if value in hashmap, ++ hashmap entry

for num in rightList:
    if num in hashmap:
        hashmap[num] += 1

simularity = 0

for num in hashmap:
    simularity += num * hashmap[num]

# 4. output solution

print(simularity)