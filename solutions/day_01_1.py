# 1. open input file
from pathlib import Path

path = Path(__file__).resolve().parent.parent / 'inputs' / 'day_01.txt'
inp = open(path)

# 2. extract numbers from file, put into 2 lists
#       - for each line:
#       - split, add both #'s to corresponding list
list1 = []
list2 = []

for line in inp:
    split = line.split()
    list1.append(int(split[0]))
    list2.append(int(split[1]))

inp.close()

# 3. sort

list1.sort()
list2.sort()

# 4. loop through & compare elements in lists, adding distance to total_distance

total_distance = 0
for i in range(0, len(list1)):
    total_distance += abs(list1[i] - list2[i])

# 5. output solution

print(total_distance)
