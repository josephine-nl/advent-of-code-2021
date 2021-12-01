def loadfile(name):
    values = []
    f = open(name, "r")
    for x in f:
        values.append(int(x))
    return values

def day1 (space):
    counter = 0
    for i in range(0, len(values) - space):
        if values[i] < values[i + space]:
            counter += 1
    return counter

values = loadfile("data.txt")
print(values)
print("solution day1a: " + str(day1(1)))
print("solution day1b: " + str(day1(3)))