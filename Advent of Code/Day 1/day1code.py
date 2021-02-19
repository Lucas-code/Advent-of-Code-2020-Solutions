import math
from itertools import combinations

numbers = []
with open("day1input.txt","r") as puzzle_input:
    for line in puzzle_input.readlines():
        numbers.append(int(line))

for n in combinations(numbers,3):
    if sum(n) == 2020:
        print(math.prod(n))
