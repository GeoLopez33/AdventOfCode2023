import re
file = open(r'..\Day_1\Input_2.txt','r')
textArray = file.readlines()


result = 0
numArray = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def getNum(x):
    if numArray.index(x) < 9:
        return numArray.index(x) + 1
    else:
        return numArray.index(x) - 8


#If the first digit is in string form, then it is replaced with it's int form. 
#Whatever the last digit is, whether string or int. It is captured/converted and copied to end of the string.
for i in range(len(textArray)):
    textArray[i] = re.sub("\n", '', textArray[i])
    
    textArray[i] = re.sub("(?:(one|two|three|four|five|six|seven|eight|nine|\d))", str(getNum(re.search("(?:(one|two|three|four|five|six|seven|eight|nine|\d))", textArray[i]).group())), textArray[i], 1)
    textArray[i] = textArray[i] + re.sub(".*(?:(one|two|three|four|five|six|seven|eight|nine|\d))", str(getNum(re.search("(.*)(?:(one|two|three|four|five|six|seven|eight|nine|\d))", textArray[i]).group(2))), textArray[i], 1)
    


#Find First Digit with Regex
p1 = re.compile("^[^\d]*(\d)")
r1 = p1.match(textArray[0])

#Find Last Digit with Regex
p2 = re.compile("^.*(\d)")
r2 = p2.match(textArray[0])



for x in textArray:
    r1 = p1.match(x)
    r2 = p2.match(x)

    #Just for testing and viewing result of Regex matches
    #print(x + r1.group(1) + r2.group(1))

    result += int(r1.group(1) + r2.group(1))



print(result)