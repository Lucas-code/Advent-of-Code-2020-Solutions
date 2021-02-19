import itertools

part1Result = 0

def checkMatch(preamble,number):
    for n in itertools.combinations(preamble,2):
        if sum(n) == number:
            return True
    return False


with open("input.txt","r") as file:
    data = [int(x) for x in file.read().split("\n")]
    data2 = data.copy()

encryptMatch = True

while encryptMatch == True:
    preamble = data[:25]
    number = data[25]
    if not checkMatch(preamble,number):
        encryptMatch = False
        print(number)
        part1Result = number
    else:
        data.pop(0)

contiguousList = []
contiguousListCorrect = False
startingIndex = 0
while not contiguousListCorrect:
    contiguousList = []
    for item in data2[startingIndex:]:
        contiguousList.append(item)
        if sum(contiguousList) == part1Result:
            contiguousListCorrect = True
            break
    startingIndex += 1

print(max(contiguousList) + min(contiguousList))
