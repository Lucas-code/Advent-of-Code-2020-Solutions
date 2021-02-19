num_count = {
    "1" : 0,
    "3" : 1
}
data = []
with open("input.txt","r") as file:
    data = [int(line.replace("\n","")) for line in file.readlines()]
    data.sort()

for num in data:
    if data.index(num) == 0:
        if num == 1:
            num_count["1"] += 1
        elif num == 3:
            num_count["3"] += 1
        continue
    else:
        previous = data[data.index(num)-1]
        difference = num - previous
        if difference == 1:
            num_count["1"] += 1
        elif difference == 3:
            num_count["3"] += 1

print(num_count["1"] * num_count["3"])
