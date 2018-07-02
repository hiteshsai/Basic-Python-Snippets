import re

def findmatches(pattern, phrase):

    for p in patterns:
        match= re.findall(p, phrase)
        print(match)

phrase= raw_input("please  enter the string you want to find :")

patterns= [r'\d+']

findmatches(patterns, phrase)
