def loadfile(name):
    lines = []
    f = open(name, "r")
    for x in f:
        if x.endswith('\n'):
            x = x[:-1]
        points = x.split(" -> ")
        line = []
        for point in points:
            p = [int(point.split(",")[0]), int(point.split(",")[1])]
            line.append(p)
        lines.append(line)
    return lines

def getStraightLines():
    straightLines = []
    for line in lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            straightLines.append(line)
    return straightLines

def getAllPointsHit(Lines):
    pointsHit = {}
    for line in Lines:
        if line[0][0] == line[1][0]:
            direction = 1 if line[0][1] < line[1][1] else -1
            for i in range(line[0][1], line[1][1] + direction, direction):
                coordinate = str(line[0][0]) + "," + str(i)
                if coordinate in pointsHit:
                    pointsHit[coordinate] = pointsHit[coordinate] + 1
                else:
                    pointsHit[coordinate] = 1
        elif line[0][1] == line[1][1]:
            direction = 1 if line[0][0] < line[1][0] else -1
            for i in range(line[0][0], line[1][0] + direction, direction):
                coordinate = str(i) + "," + str(line[0][1])
                if coordinate in pointsHit:
                    pointsHit[coordinate] = pointsHit[coordinate] + 1
                else:
                    pointsHit[coordinate] = 1
        elif (line[0][0] - line[1][0] == line[0][1] - line[1][1]):
            c = line[0] if line[0][0] < line [1][0] else line[1]
            endpoint = line[0] if line[0][0] > line [1][0] else line[1]
            notConnectedToEndPoint = True
            while notConnectedToEndPoint:
                coordinate = str(c[0]) + "," + str(c[1])
                if coordinate in pointsHit:
                    pointsHit[coordinate] = pointsHit[coordinate] + 1
                else:
                    pointsHit[coordinate] = 1
                if c[0] == endpoint[0] and c[1] == endpoint[1]:
                    notConnectedToEndPoint = False
                c[0] = c[0] + 1
                c[1] = c[1] + 1
        elif (line[0][0] - line[1][0] == line[1][1] - line[0][1]):
            c = line[0] if line[0][0] < line [1][0] else line[1]
            endpoint = line[0] if line[0][0] > line [1][0] else line[1]
            notConnectedToEndPoint = True
            while notConnectedToEndPoint:
                coordinate = str(c[0]) + "," + str(c[1])
                if coordinate in pointsHit:
                    pointsHit[coordinate] = pointsHit[coordinate] + 1
                else:
                    pointsHit[coordinate] = 1
                if c[0] == endpoint[0] and c[1] == endpoint[1]:
                    notConnectedToEndPoint = False
                c[0] = c[0] + 1
                c[1] = c[1] - 1
        else:
            print("ERROR")
            print("Line: ", str(line))
    return pointsHit

def getAmountPointsMoreThenOne(hitPoints):
    counter = 0
    for coordinate, hits in hitPoints.items():
        if hits > 1:
            counter += 1
    return counter

lines = loadfile("data.txt")
straightLines = getStraightLines()

hitPointsStraight = getAllPointsHit(straightLines)
amountStraight = getAmountPointsMoreThenOne(hitPointsStraight)

hitPoints = getAllPointsHit(lines)
amount = getAmountPointsMoreThenOne(hitPoints)

print("solution day3a: " + str(amountStraight))
print("solution day3b: " + str(amount))