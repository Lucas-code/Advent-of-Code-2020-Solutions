from itertools import combinations

def check(iterable):
    for item in iterable:
        if iterable.index(item) > 0:
            prev = iterable[iterable.index(item) - 1]
            diff = item - prev
            if diff > 3:
                return False
            else:
                continue
    return True

data = []
with open("example_input_short.txt","r") as file:
    data = [int(line.rstrip()) for line in file.readlines()]
    data.sort()

correct = 0

for num in range(len(data),-1,-1):
    for adapters in combinations(data,num):
        if check(adapters):
            correct += 1

print(correct)


#This solution doesn't work :(
#With this input the answer should be 8 but I got 170
