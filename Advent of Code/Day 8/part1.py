data = []
executed = set()
with open("input.txt","r") as file:
    for cmd in file.read().split("\n"):
        data.append(cmd.split(" "))

i = 0
acc = 0
while i < len(data):
    current_len = len(executed)
    executed.add(i)
    if len(executed) == current_len:
        break
    if data[i][0] == "acc":
        acc += int(data[i][1])
        i += 1
    elif data[i][0] == "jmp":
        i += int(data[i][1])
    else:
        i+= 1
print(acc)
