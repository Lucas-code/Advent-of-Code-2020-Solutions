##import re
##
##rawdata = []
##required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
##with open("input.txt","r") as file:
##    num = 1
##    rawdata = file.read().split("\n\n")
##    #print(rawdata)
##    #rawdata = [line.replace("\n","").split() for line in rawdata]
##    rawdata = [line.split() for line in rawdata]
##    for entry in range(len(rawdata)):
##        for field in range(len(rawdata[entry])):
##            rawdata[entry][field] = rawdata[entry][field].split(":")
####        data[num] = {(field.split(":")[0] for field in entry) : (field.split(":")[1] for field in entry)}
####        num += 1
##    #print(rawdata)
##
##successful = 0
##
##def validate(item):
##    for field in item:
##        if field[0] == "byr":
##            if int(field[1]) < 1920 or int(field[1]) > 2002:
##                return False
##        elif field[0] == "iyr":
##            if int(field[1]) < 2010 or int(field[1]) > 2020:
##                return False
##        elif field[0] == "eyr":
##            if int(field[1]) < 2020 or int(field[1]) > 2030:
##                return False
##        elif field[0] == "hgt":
##            if field[1][-2:] == "cm":
##                if int(field[1][:-2]) < 150 or int(field[1][:-2]) > 193:
##                    return False
##            elif field[1][-2:] == "in":
##                if int(field[1][:-2]) < 59 or int(field[1][:-2]) > 76:
##                    return False
##        elif field[0] == "hcl":
##            if not re.match(r'#[\da-f]{6}',field[1]):
##                return False
##        elif field[0] == "ecl":
##            if field[1] not in ["amb","blu","brn","gry","grn","hzl","oth"]:
##                return False
##        elif field[0] == "pid":
##            if not re.match(r"\d{9}",field[1]):
##                return False
##        else:
##            continue
##    return True
##    
##def correct_fields(item):
##    meets_crit = 0
##    correct_entries =[]
##    for entry in item:
##        for field in entry:
##            if field[0] not in required_fields:
##                if field[0] == "cid":
##                    continue
##                else:
##                    meets_crit -= 1
##            else:
##                continue
##        if meets_crit < 0:
##            continue
##        else:
##            correct_entries.append(entry)
##    print(len(correct_entries))
##    return correct_entries
##            
##        
##
##
##for entry in correct_fields(rawdata):
##    if validate(entry):
##        successful += 1
##        print(entry) 
##
##print(successful)

#Solution copied from reddit
import re

with open('input.txt', 'r') as file:
    lst = file.read().split('\n\n')
    lst = [x.replace('\n', ' ').split() for x in lst]
    passports = []
    for person in lst:
        passports.append(dict(data.split(':') for data in person))

    passports = [x for x in passports if len(x.keys()) == 8 or (len(x) == 7 and 'cid' not in x.keys())]
    #print(len(passports))

    # Part 2
    valid_passports = []

    values = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for person in passports:
        if (1920 <= int(person['byr']) <= 2002
                and (2010 <= int(person['iyr']) <= 2020)
                and (2020 <= int(person['eyr']) <= 2030)
                and
                ((person['hgt'][-2:] == 'cm' and 150 <= int(person['hgt'][:-2]) <= 193)
                 or (person['hgt'][-2:] == 'in' and 59 <= int(person['hgt'][:-2]) <= 76))
                and (re.match(r'#[\da-f]{6}', person['hcl']))
                and (person['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
                and (re.match(r'\d{9}', person['pid']))):
            valid_passports.append(person)

print(len(valid_passports) - 1)
