data = []
#executed = set()
with open("input.txt","r") as file:
    for cmd in file.read().split("\n"):
        data.append(cmd.split(" "))

successful = False
def test_data():
    i = 0
    acc = 0
    executed = set()
    while True:
        try:
            current_len = len(executed)
            executed.add(i)
            if len(executed) == current_len:
                print("Failure")
                break
            if data[i][0] == "acc":
                acc += int(data[i][1])
                i += 1
            elif data[i][0] == "jmp":
                i += int(data[i][1])
            else:
                i+= 1
        except IndexError:
            print("Success!")
            global successful
            successful = True
            print(acc)

def change_value(line):
    if line[0] == "jmp":
        line[0] = "nop"
    elif line[0] == "nop":
        line[0] = "jmp"

while successful == False:
    for line in data:
        if line[0] == "jmp" or line[0] == "nop":
            change_value(line)
            test_data()
            change_value(line)
