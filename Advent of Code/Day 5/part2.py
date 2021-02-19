from math import ceil
from itertools import combinations

IDs = []
with open("input.txt","r") as file:
    for line in file.readlines():
        lowest_row = 1
        highest_row = 126
        for rows in line[:7]:
            if rows == "F":
                highest_row = lowest_row + int((highest_row-lowest_row)/2)
            elif rows == "B":
                lowest_row = lowest_row + ceil((highest_row-lowest_row)/2)
        if highest_row == lowest_row:
            final_row = highest_row
        else:
            print("Something went wrong with rows..")
        lowest_col = 0
        highest_col = 7
        for cols in line[7:10]:
            if cols == "R":
                lowest_col = lowest_col + ceil((highest_col-lowest_col)/2)
            elif cols == "L":
                highest_col = lowest_col + int((highest_col-lowest_col)/2)
        if highest_col == lowest_col:
            final_col = highest_col
        else:
            print("Something went wrong with cols..")
        IDs.append(final_row * 8 + final_col)

#print(max(IDs))


for n in combinations(IDs,2):
    if abs(n[0]-n[1]) == 2 and int((n[0]+n[1])/2) not in IDs:
        print(int((n[0]+n[1])/2))


