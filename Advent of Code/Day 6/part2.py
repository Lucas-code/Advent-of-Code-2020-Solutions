with open("input.txt","r") as file:
    count = 0
    for groups in [x.split("\n") for x in file.read().split("\n\n")]:
        group = [set(persons) for persons in groups]
        if len(group) == 1:
            print(f"number of matches: {len(group[0])} - matches: {group[0]}")
            count += len(group[0])
        else:
            count += len(group[0].intersection(*group))
            print(f"number of matches: {len(group[0].intersection(*group))} - matches: {group[0].intersection(*group)}")
    print(count)

    
