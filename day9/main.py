import pandas as pd
def loadfile(name):
    lines = []
    file = open(name, "r")
    for row in file:
        if row.endswith('\n'):
            row = row[:-1]
        line = []
        for character in list(row):
            line.append(int(character))
        lines.append(line)
    return lines

def getNeighboursCoords(lines, pointsInBassin, i, j):
    neighbours = []
    if(i > 0 and not lines[i - 1][j] == 9 and coorToString([i - 1, j]) not in pointsInBassin):
        pointsInBassin.append(coorToString([i - 1, j]))
        neighbours.append([i - 1, j])
        neighbours.extend(getNeighboursCoords(lines, pointsInBassin, i - 1, j))

    if(i < len(lines) - 1 and not lines[i + 1][j] == 9 and coorToString([i + 1, j]) not in pointsInBassin):
        pointsInBassin.append(coorToString([i + 1, j]))
        neighbours.append([i + 1, j])
        neighbours.extend(getNeighboursCoords(lines, pointsInBassin, i + 1, j))

    if j > 0 and not lines[i][j - 1] == 9 and coorToString([i, j - 1]) not in pointsInBassin :
        pointsInBassin.append(coorToString([i, j - 1]))
        neighbours.append([i, j - 1])
        neighbours.extend(getNeighboursCoords(lines, pointsInBassin, i, j - 1))

    if (j < len(lines[0]) - 1 and not lines[i][j + 1] == 9 and coorToString([i, j + 1]) not in pointsInBassin):
        pointsInBassin.append(coorToString([i, j + 1]))
        neighbours.append([i, j + 1])
        neighbours.extend(getNeighboursCoords(lines, pointsInBassin, i, j + 1))
    return neighbours

def getNeighbours(lines, i, j):
    neighbours = []
    if(i > 0):
        neighbours.append(lines[i - 1][j])
    if(i < len(lines) - 1):
        neighbours.append(lines[i + 1][j])
    if(j > 0):
        neighbours.append(lines[i][j - 1])
    if (j < len(lines[0]) - 1):
        neighbours.append(lines[i][j + 1])
    return neighbours

def getLargestBassin(lines, lowestPoints):
    bassins = []
    for lowestPoint in lowestPoints:
        counter = 1
        pointsInBassin = []
        pointsInBassin.append(coorToString(lowestPoint))
        neighbours = getNeighboursCoords(lines, pointsInBassin, lowestPoint[0], lowestPoint[1])
        bassins.append(len(neighbours) + 1)
    return bassins

def coorToString(coor):
    return str(coor[0]) + "," + str(coor[1])

def isLowestPoint(lines, i, j):
    current = lines[i][j]
    neighbours = getNeighbours(lines, i, j)
    for neighbour in neighbours:
        if neighbour <= current:
            return False
    return True

def findLowestPoints(lines):
    lowestPointsValues = []
    lowestPoints = []
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if isLowestPoint(lines, i, j):
                lowestPointsValues.append(lines[i][j] + 1)
                lowestPoints.append([i, j])
    return [lowestPointsValues, lowestPoints]

lines = loadfile("data.txt")
[lowestPointsValues, lowestPoints] = findLowestPoints(lines)
print("Opdracht 9a: ",sum(lowestPointsValues))

result = sorted(getLargestBassin(lines, lowestPoints))
print("Opdracht 9b: ", result[-1]*result[-2]*result[-3])


