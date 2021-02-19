#can be used for both 1 and 2
from math import prod
data = []
with open("input.txt","r") as file:
    for line in file.readlines():
        add = []
        for char in line[:-1]:
            add.append(char)
        data.append(add)
        
def find_trees(step,down_num):
    xindex = 0
    trees = 0

    for line in data[down_num::down_num]:
        max_index = len(line) - 1
        xindex += step
        while xindex > max_index:
            line.extend(line)
            max_index = max_index*2
        if line[xindex] == "#":
            trees += 1

    return trees

rules = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]

results = []
for rule in rules:
    results.append(find_trees(rule[0],rule[1]))

print(results)
print(prod(results))
