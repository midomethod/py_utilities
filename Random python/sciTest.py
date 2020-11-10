"""
This module calculates the proability of all unique birthdays in a group
using functions from scientific.py
"""

import scientific as sci


"""
i = 0
while i<=20:
    fac = sci.sciFactorial(i)

    if fac.getME()[1]<=6:
        print("{}!\t= {}".format(i,sci.sciToInt(fac)))
    else:
        print("{}!\t= {}".format(i,fac))
    i+=1
"""

for i in range(1,101):
    Prob = sci.birthday(i)

    if Prob<1:
        strP = "{:f}".format(Prob)
    else:
        strP = "{:.2f}".format(Prob)

    print("i = {}\tP = {}%".format(i,strP))