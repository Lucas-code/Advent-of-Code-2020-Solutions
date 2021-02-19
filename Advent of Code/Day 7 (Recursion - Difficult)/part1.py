import re

count = 0

def solve(file,string):
    global count
    for line in file:
        if re.match(string,line):
            file.remove(line)
            count += 1
        if string in line and not re.match(string,line):
            count += 1
            new_string = line.split(" ")[0] + " " + line.split(" ")[1]
            data.remove(line) 
            solve(file,new_string)
    return count

with open("input.txt","r") as file:
    data = [x for x in file.read().split("\n")]
    print(solve(data,"shiny gold"))
