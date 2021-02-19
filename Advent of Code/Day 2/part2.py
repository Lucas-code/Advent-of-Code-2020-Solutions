import re

def get_policy_info(key):
    dash = key.find("-")
    minimum = int(key[:dash])
    maximum = int(key[dash+1:-2])
    char = key[-1]
    return [minimum,maximum,char]

def meets_policy(value,minimum,maximum,char):
    if len(re.findall(char,value)) >= minimum and len(re.findall(char,value)) <= maximum:
        return True
    else:
        return False

count = 0
with open("input.txt","r") as file:
    for line in file.readlines():
        split = line.split(":")
        modified_val = split[1][1:]
        info = get_policy_info(split[0])
        if meets_policy(modified_val,info[0],info[1],info[2]):
            count += 1
        else:
            continue
        
print(count)

file.close()
