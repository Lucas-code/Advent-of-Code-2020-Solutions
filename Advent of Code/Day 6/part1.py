with open("input.txt","r") as file:
    count = 0
    for group in ["".join(x.replace("\n","")) for x in file.read().split("\n\n")]:
        distinct_ans = set()
        for letter in group:
            distinct_ans.add(letter)
        count += len(distinct_ans)

print(count)
