
import re
lines = []
with open('Studierendendaten.txt') as f:
    lines = f.readlines()

for line in lines:
    #not white space characters=>get the first word in line
    degree = re.findall("^\S*",line) 
    fdNumber = re.findall('^(?:\\w+\\W+){1}(\\w+)',line) 
    name = re.findall('^(?:\\w+\\W+){2}(\\w+)',line) 

    # for el in degree:
    #     if el != "Master" and el != "Bachelor":
    #         print(el)

    for el in name:
            print(el) 

            