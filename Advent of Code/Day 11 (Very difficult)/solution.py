from copy import deepcopy
import numpy as np

with open("input.txt","r") as file:
    grid = [list(row.rstrip().split()[0]) for row in file.readlines()]


adjacent = [(1,0),(1,-1),(1,1),(0,-1),(0,1),(-1,0),(-1,-1),(-1,1)]

part2_adjacent = [[(1,0)],[(1,-1)],[(1,1)],[(0,-1)],[(0,1)],[(-1,0)],[(-1,-1)],[(-1,1)]]

def part1():
    while True:
        prev_grid = deepcopy(grid)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                occupied = 0
                seat = grid[row][col]
                for adj in adjacent:
                    try:
                        adj_row_pos = row + adj[0]
                        adj_col_pos = col + adj[1]
                        if adj_row_pos < 0 or adj_col_pos < 0:
                            continue
                        elif prev_grid[adj_row_pos][adj_col_pos] == "#":
                            occupied += 1
                    except IndexError:
                        continue
                if occupied == 0 and seat == "L":
                    grid[row][col] = "#"
                elif occupied >= 4 and seat == "#":
                    grid[row][col] = "L"
        if prev_grid == grid:
            final_occupied = 0
            for row in grid:
                final_occupied += row.count("#")
            print(final_occupied)
            break

def part2():
    while True:
        prev_grid = deepcopy(grid)
        rows_len = len(grid)
        col_len = len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                occupied = 0
                seat = grid[row][col]
                for adj in adjacent:
                    row_val = adj[0]
                    col_val = adj[1]
                    while True:
                        try:
                            adj_row_pos = row + row_val
                            adj_col_pos = col + col_val
                            if adj_row_pos < 0 or adj_col_pos < 0:
                                break
                            elif prev_grid[adj_row_pos][adj_col_pos] == "#":
                                occupied += 1
                                break
                            elif prev_grid[adj_row_pos][adj_col_pos] == "L":
                                break
                            else:
                                row_val += adj[0]
                                col_val += adj[1]
                        except IndexError:
                            break
                if occupied == 0 and seat == "L":
                    grid[row][col] = "#"
                elif occupied >= 5 and seat == "#":
                    grid[row][col] = "L"
        if prev_grid == grid:
            final_occupied = 0
            for row in grid:
                final_occupied += row.count("#")
            print(final_occupied)
            break

part2()
