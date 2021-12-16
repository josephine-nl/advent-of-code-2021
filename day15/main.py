import random
import math

def loadfile(name):
    lines = []
    f = open(name, "r")
    for x in f:
        if x.endswith('\n'):
            x = x[:-1]
        line = []
        for i in x:
            line.append(int(i))
        lines.append(line)
    return lines


def getPossibleMoves(position, matrix):
    possibleMoves = []
    [i,j] = position
    if(i > 0):
        possibleMoves.append([i - 1, j])
    if(i < len(matrix) - 1):
        possibleMoves.append([i + 1, j])
    if(j > 0):
        possibleMoves.append([i, j - 1])
    if (j < len(matrix[0]) - 1):
        possibleMoves.append([i, j + 1])
    #print(possibleMoves)
    return possibleMoves


def makeEmptyMatrix(l, w):
    m = []
    for i in range(l):
        m.append([0] * w)
    return m


def makeBigMatrix (matrix):
    bigMatrix = makeEmptyMatrix(len(matrix) * 5, len(matrix) * 5)
    for i in range(0, len(bigMatrix)):
        for j in range(0, len(bigMatrix[i]) ):
            k =  i % (len(matrix) )
            m =  j % (len(matrix) )
            print(math.floor((j + i + -1 )/(len(matrix))))
            print("ji", j, i)
            print("len", len(matrix))

            value =  matrix[k][m] + (math.floor(j / len(matrix)) + math.floor(i / len(matrix)))
            print("val", value)
            if value > 9:
                value = value - 9
            bigMatrix[i][j] = value
    return bigMatrix


def getShortestRoute(matrix):
    lowestCost = 0
    # lets go backwards
    start = [0,0]
    end = [len(matrix) - 1, len(matrix) - 1]

    positionCost = {}
    foundLowestCost = False
    lastPositions = [end]
    positionCost[str(len(matrix) - 1) + '-' + str(len(matrix) - 1)] = matrix[len(matrix) - 1][len(matrix) - 1]
    print("end", end)
    while not foundLowestCost:
        foundLowestCost = True
        positions = []
        for position in lastPositions:
            pKey = str(position[0]) + "-" + str(position[1])
            nextPositions = getPossibleMoves(position, matrix)
            for nPosition in nextPositions:
                cost = positionCost[pKey] + matrix[nPosition[0]][nPosition[1]]
                key = str(nPosition[0]) + "-" + str(nPosition[1])
                if key in positionCost:
                    if cost < positionCost[key]:
                        positionCost[key] = cost
                        positions.append(nPosition)
                        foundLowestCost = False
                else:
                    positionCost[key] = cost
                    positions.append(nPosition)
                    foundLowestCost = False

        lastPositions = positions

    print(positionCost)
    return positionCost["0-0"] - matrix[0][0],


matrix = loadfile("data.txt")
print(matrix)

shortestRoute = getShortestRoute(matrix)
shortestRoute = 0
print("Opdracht 15a: ", shortestRoute)

bigMatrix = makeBigMatrix(matrix)
print(bigMatrix)
print(len(bigMatrix) - 1, len(bigMatrix) - 1)

shortestRoute = getShortestRoute(bigMatrix)
print(bigMatrix)
print("Opdracht 15b: ", shortestRoute)