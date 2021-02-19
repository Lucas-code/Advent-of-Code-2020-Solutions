import re

from itertools import chain

#print([i for i in chain()])

from collections.abc import Iterable
def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

def eval_float(value):
    if not "X" in value:
        #print(value)
        return int("".join(value),2)
    else:
        x_index = value.index('X')
        return eval_float(value[:x_index]+['0']+value[x_index+1:]),eval_float(value[:x_index]+['1']+value[x_index+1:])

def apply_bitmask(binary,mask,part):
    if part == 1:
        split_binary = [letter for letter in binary]
        search_num = 0
        while mask.find("1",search_num) != -1:
            split_binary[mask.find("1",search_num)] = "1"
            search_num = mask.find("1",search_num)+1
        search_num = 0
        while mask.find("0",search_num) != -1:
            split_binary[mask.find("0",search_num)] = "0"
            search_num = mask.find("0",search_num)+1
        answer = "".join(split_binary)
        return answer
    if part == 2:
        split_binary = [letter for letter in binary]
        #print(split_binary.count('0'),split_binary,"\n",binary)
        search_num = 0
        while mask.find("1",search_num) != -1:
            split_binary[mask.find("1",search_num)] = "1"
            search_num = mask.find("1",search_num)+1
        x_indexes = [i for i,x in enumerate(mask) if x == "X"]
        for x in x_indexes:
            split_binary[x] = 'X'
        #print(split_binary)
        addresses = list(flatten(eval_float(split_binary)))
        return addresses
    else:
        raise Exception("Third parameter must be 1 or 2 (integer too!!)")

#print(apply_bitmask('{:036b}'.format(57319),'0010011010X1000100X101011X10010X1010',2))


with open("input.txt","r") as file:
    program = [line.rstrip() for line in file.readlines()]

def part1():
    memory = {}
    for line in program:
        if line[:4] == "mask":
            mask = line[7:]
        else:
            memory_location = re.split(r"\[|\]",line)[1]
            initial_val = int(re.split(r"\[|\]",line)[2][3:])
            binary_val = '{:036b}'.format(initial_val)
            final_val = int(apply_bitmask(binary_val,mask,1),2)
            memory[memory_location] = final_val
    return sum(memory.values())

def part2():
    memory = {}
    for line in program:
        if line[:4] == "mask":
            mask = line[7:]
        else:
            memory_location = int(re.split(r"\[|\]",line)[1])
            #print(memory_location)
            value = int(re.split(r"\[|\]",line)[2][3:])
            memory_locations = apply_bitmask('{:036b}'.format(memory_location),mask,2)
            #print(f"Value to be added: {value} --- Memory locations: {memory_locations}")
            for location in memory_locations:
                memory[location] = value
    #print(memory)
    return sum(memory.values())

print(part2())


