def loadfile(name):
    lines = []
    f = open(name, "r")
    for x in f:
        if x.endswith('\n'):
            x = x[:-1]
        line = []
        for character in x:
            line.append(int(character))
        lines.append(line)
    return lines

def add1ToAll(lines):
    for i in range (0, len(lines)):
        for j in range(0, len(lines[i])):
            lines[i][j] = lines[i][j] + 1
    return lines


neighbours = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [1, 1], [0, 1], [-1, 1]]

def flash(i, j):
    lines[i][j] = 0
    count = 1
    for coor in neighbours:
        if i + coor[0] >= 0 and i + coor[0] < len(lines) and j + coor[1] >= 0 and j + coor[1] < len(lines[0]):
            if lines[i + coor[0]][j + coor[1]] != 0:
                lines[i + coor[0]][j + coor[1]] += 1
                if lines[i + coor[0]][j + coor[1]] > 9:
                    count += flash(i + coor[0], j + coor[1])
    return count

def makeOctopusFlash():
    count = 0
    for i in range (0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] > 9:
                count += flash(i, j)

    return count

def goThroughSteps (lines, steps):
    countFlashes = 0
    for step in range(1, steps + 1):
        lines = add1ToAll(lines)
        count = makeOctopusFlash()
        print("Step: ", step, " Flashes: ", count)
        countFlashes += count
    return countFlashes

def findAllFlash(lines):
    countFlashes = 0
    found = False
    step = 1
    while found == False:
        lines = add1ToAll(lines)
        count = makeOctopusFlash()
        print("Step: ", step, " Flashes: ", count)
        if count == 100:
            return step
        countFlashes += count
        step += 1
    return 0


lines = loadfile("data.txt")
print(lines)
flashes = goThroughSteps(lines, 100)
lines = loadfile("data.txt")
step = findAllFlash(lines)
print("Opdracht 11a: ", flashes)
print("Opdracht 11b: ", step)