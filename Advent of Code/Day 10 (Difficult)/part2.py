from itertools import combinations
data = []
with open("input.txt","r") as file:
    data = [int(line.rstrip()) for line in file.readlines()]
    data.sort()

data.append(max(data)+3)

counter = {0:1}

for adapter in data:
    counter[adapter] = counter.get(adapter-3,0)+counter.get(adapter-2,0)+counter.get(adapter-1,0)
    
print(f"The answer for part 2 is: {counter[data[-1]]}")


