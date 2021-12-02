def loadfile(name):
    values = []
    f = open(name, "r")
    for x in f:
        values.append(x)
    return values

def day2():
    depth = 0
    position = 0
    depth2 = 0
    for i in range(0, len(values)):
        value = values[i].split()
        if value[0] == "forward":
            position += int(value[1])
            depth2 += int(value[1]) * depth
        elif value[0] == "down":
            depth += int(value[1])
        elif value[0] == "up":
            depth -= int(value[1])
    return [position,depth, depth2]


values = loadfile("data.txt")
print(values)
solution = day2()
print("full solution: " + str(solution))
print("solution day2a: " + str(solution[0]*solution[1]))
print("solution day2b: " + str(solution[0]*solution[2]))