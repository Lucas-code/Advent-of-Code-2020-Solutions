rawdata = []
required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
with open("input.txt","r") as file:
    num = 1
    rawdata = file.read().split("\n\n")
    #print(rawdata)
    
def valid(item):
    for field in required_fields:
        if field not in item:
            return False
    return True


print(rawdata)
is_valid = 0

for item in rawdata:
    if valid(item):
        is_valid += 1

print(is_valid)
    
