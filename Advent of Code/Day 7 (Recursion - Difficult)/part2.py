import re

result = 0

##def solve(file,string):
##    global result
##    for line in file:
##        if re.match(string,line):
##            bags_in_bag = re.findall(r"(\d+?) (.+?) bags?", line)
##            if bags_in_bag:
##                for bag in bags_in_bag:
##                    print(bag)
##                    result += int(bag[0])
##                    result += int(bag[0]) * solve(file,bag[1])
##            else:
##                return 0
            
        
data_dic = {}
with open("input.txt","r") as file:
    data = [x for x in file.read().split("\n")]
    for line in data:
        colour = re.match(r"(.+?) bags contain", line)[1]  
        data_dic[colour] = re.findall(r"(\d+?) (.+?) bags?", line)
    print(data_dic)

def count_bags(bag_type):
    return 1 + sum(int(number)*count_bags(colour) for number, colour in data_dic[bag_type])

print(f"result = {count_bags('shiny gold')-1}")
print(1 + sum(None))
