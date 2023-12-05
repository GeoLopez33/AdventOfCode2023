import re
file = open(r'..\Day_1\Input_1.txt','r')
textArray = file.readlines()


result = 0

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