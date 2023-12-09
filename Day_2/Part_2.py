import numpy as np
import re
file = open(r"E:\AdventOfCode2023\Day_2\Input_1.txt",'r')
textArray = file.readlines()

result = 0


for i in range(len(textArray)):

    testRed = re.findall("\d+(?=\sred)", textArray[i])
    testGreen = re.findall("\d+(?=\sgreen)", textArray[i])
    testBlue = re.findall("\d+(?=\sblue)", textArray[i])

    plusFlag = 0

    plusFlag = np.max([eval(i) for i in testRed]) * np.max([eval(i) for i in testGreen]) * np.max([eval(i) for i in testBlue])
    

    result += plusFlag



print(result)