with open("input.txt","r") as file:
    pa_system = [action.rstrip() for action in file.readlines()]

def part1():
    ship_pos = [0,0,"East"]
    directions = ["North","East","South","West"]
    for actions in pa_system:
        action = actions[0]
        quantity = int(actions[1:])
        if action in "NESW":
            if action == "N":
                ship_pos[1] += quantity
            elif action == "E":
                ship_pos[0] += quantity
            elif action == "S":
                ship_pos[1] -= quantity
            else:
                ship_pos[0] -= quantity
        elif action in "LR":
            current_rotation = directions.index(ship_pos[2])
            rotation_change = quantity / 90
            if action == "L":
                rotation_change *= -1
            if rotation_change + current_rotation < 0:
                rotation_change += 4
            elif rotation_change + current_rotation > 3:
                rotation_change -= 4
            ship_pos[2] = directions[int(rotation_change + current_rotation)]
        elif action == "F":
            if ship_pos[2] == "North":
                ship_pos[1] += quantity
            elif ship_pos[2] == "East":
                ship_pos[0] += quantity
            elif ship_pos[2] == "South":
                ship_pos[1] -= quantity
            elif ship_pos[2] == "West":
                ship_pos[0] -= quantity
    return abs(ship_pos[0]) + abs(ship_pos[1])

#print(part1())

def part2():
    ship_pos = [0,0]
    waypoint_pos = [10,1]
    for actions in pa_system:
        action = actions[0]
        quantity = int(actions[1:])
        if action in "NESW":
            if action == "N":
                waypoint_pos[1] += quantity
            elif action == "E":
                waypoint_pos[0] += quantity
            elif action == "S":
                waypoint_pos[1] -= quantity
            else:
                waypoint_pos[0] -= quantity
        elif action in "LR":
            rotation_change = quantity / 90
            if action == "L":
                rotation_change *= -1
            if rotation_change % 2 == 0:
                waypoint_pos[0] *= -1
                waypoint_pos[1] *= -1
            else:
                for _ in range(int(abs(rotation_change))):
                    if action == "L":
                        waypoint_pos[0],waypoint_pos[1] = waypoint_pos[1]*-1,waypoint_pos[0]
                    elif action == "R":
                        waypoint_pos[0],waypoint_pos[1] = waypoint_pos[1],waypoint_pos[0]*-1
        elif action == "F":
            ship_pos[0] += waypoint_pos[0] * quantity
            ship_pos[1] += waypoint_pos[1] * quantity
    return abs(ship_pos[0]) + abs(ship_pos[1])

print(part2())
