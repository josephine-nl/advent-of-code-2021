import re


def loadfile(name):
    values = []
    f = open(name, "r")
    for x in f:
        values.append(int(x))
    f.close()
    return values

def day1a ():
    counter = 0
    for i in range(1, len(values)):
        if values[i - 1] < values[i]:
            counter += 1
    return counter



def day1b():
    counter = 0
    for i in range(0, len(values) - 3):
        windowA = values[i] + values[i + 1] + values[i + 2]
        windowB = values[i + 1] + values[i + 2] + values[i + 3]
        if windowA < windowB:
            counter += 1
    return counter

values = loadfile("data.txt")
print(values)
print("solution day1a: " + str(day1a()))
print("solution day1b: " + str(day1b()))