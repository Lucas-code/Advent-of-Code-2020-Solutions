from collections.abc import Iterable
def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

puzzle_input = [20,0,1,11,6,3]
def part1():
    for i in range(len(puzzle_input),2020):
        prev_val = puzzle_input[i-1]
        if puzzle_input.count(prev_val) == 1:
            puzzle_input.append(0)
        else:
            if prev_val == puzzle_input[i-2]:
                puzzle_input.append(1)
            else:
                reversed_list = list(reversed(puzzle_input[:i-1]))
                #print("reversed: ",reversed_list,"\nindex:",reversed_list.index(prev_val))
                #answer = reversed_list.index(prev_val) - len(reversed_list[:reversed_list.index(prev_val)])
                answer = len(reversed_list[:reversed_list.index(prev_val)+1])
                puzzle_input.append(answer)
                #print(puzzle_input[
##        if len(puzzle_input) % 1000 == 0:
##            print(puzzle_input[-1])
    print(puzzle_input[-1])



def part2():
    turn = 1
    ult = {}
    penul = {}
    # seed the tables
    for i in range(len(puzzle_input)):
        ult[puzzle_input[i]] = turn
        penul[puzzle_input[i]] = 0
        turn += 1
        
    target = puzzle_input[-1]
    while turn <= 30000000:
        if penul[target] == 0: # first time spoken
            target = 0
            penul[target] = ult[target]
            ult[target] = turn
        else:
            num = ult[target] - penul[target]
            target = num
            if target not in ult.keys():
                penul[target] = 0
                ult[target] = turn
            else:
                penul[target] = ult[target]
                ult[target] = turn
        turn += 1
    print(target)

part2()

