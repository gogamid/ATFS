# This program read data from file 
# and checks the fields with regular expressions
# not matched data will be ouputted
# progress right now 98/100
# https://github.com/gogamid/ATFS/tree/main/Testat1
# Author: Imron Gamidli
import re
import numpy
lines = []
c = 0
with open('Studierendendaten.txt') as f:
    lines = f.readlines()

def getError(txt, regex):
    x = re.match(regex, txt)
    if not x:
        global c
        c = c+1
        print("Fehler\t"+str(c)+":\t"+txt)

for line in lines:
    datenfelder = line.split("\t")
    getError(datenfelder[0], "Bachelor|Master")                                                         #abschluss 5
    getError(datenfelder[1], "^fd((ai)|(ei)|(lt)|(pg)|(wi))[0-9]{4}$")                                  #fd nummer 14
    getError(datenfelder[2], "^([A-Z][a-z]+)([ -][A-Z][a-z]+){0,}\s([A-Z][a-z]+)([ -][A-Z][a-z]+)?$")   #name 15
    getError(datenfelder[3], "^(?:(3[01]|[12][0-9]|0[1-9])\.(1[0-2]|0[1-9]))\.[0-9]{4}$")               #birth date 17
    getError(datenfelder[4], "^((\+[1-9][0-9]?\s)|0)[0-9]+\s[0-9]+(-[0-9]+)?$")                         #tel 19
    getError(datenfelder[5], "^[A-Za-z0-9.,_-]+@([A-Za-z0-9]{1}[A-Za-z0-9.,_-]+\.)+[a-z]{2,3}$")        #email 19
    getError(datenfelder[6], "^(?=.*[!\"&$%&\/()?._\\-])(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*")           #password 9
   

  
