import numpy as np
import re
file = open(r"E:\AdventOfCode2023\Day_2\Input_1.txt",'r')
textArray = file.readlines()

result = 0

redLimit = 12
greenLimit = 13
blueLimit = 14


for i in range(len(textArray)):

    testRed = re.findall("\d+(?=\sred)", textArray[i])
    testGreen = re.findall("\d+(?=\sgreen)", textArray[i])
    testBlue = re.findall("\d+(?=\sblue)", textArray[i])

    plusFlag = 1

    if np.max([eval(i) for i in testRed]) > redLimit:
        plusFlag = 0
    elif np.max([eval(i) for i in testGreen]) > greenLimit:
        plusFlag = 0
    elif np.max([eval(i) for i in testBlue]) > blueLimit:
        plusFlag = 0

    if plusFlag == 1:
        result += i+1



print(result)