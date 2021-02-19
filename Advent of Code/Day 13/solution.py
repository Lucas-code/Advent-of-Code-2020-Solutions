import math

with open("input.txt","r") as file:
    data = [line.rstrip() for line in file.readlines()]

def part1():
    earliest_time = int(data[0])-1
    buses = data[1].split(",")
    bus_found = False
    while not bus_found:
        earliest_time += 1
        for bus in buses:
            if bus == "x":
                continue
            else:
                if earliest_time % int(bus) == 0:
                    bus_num = int(bus)
                    bus_found = True
                    break
                continue
    waiting_time = earliest_time - int(data[0])
    answer = waiting_time * bus_num
    return answer

#print(part1())

def part2():
    buses = data[1].split(",")
    bus_nums = [int(x) for x in buses if x!= "x"]
    #print(bus_nums)
    answer = 100000000000000 #solution will be greater than this value
    answer_found = False
    while not answer_found:
        #print(answer)
        if answer % int(buses[0]) == 0:
            for index in range(len(buses)):
                #print(f"Current index: {index}")
                try:
                    if (answer + index) % int(buses[index]) == 0:
                        if index == len(buses)-1:
                            answer_found = True
                        else:
                            continue
                    else:
                        answer += math.prod([int(i) for i in buses[:index] if i != "x"])#int(buses[0])
                        break
                except ValueError:
                    continue
        else:
            answer += 1
    return answer

print(part2())
