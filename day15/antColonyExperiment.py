import random

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

def getStraightDiagonal(matrix):
    route = 0
    for i in range(0, len(matrix)):
       route = route + matrix[i][i]
       print(matrix[i][i])
       if(i + 1 < len(matrix)):
           route = route + matrix[i + 1][i]
           print(matrix[i + 1][i])
    print(route)
    return route


def ant(matrix, pheromoneMatrix, randomRange):
    start =  [0,0]
    end = [len(matrix) - 1, len(matrix[0]) - 1]
    position = start
    atEnd = False
    path = []
    costPath = 0
    while not atEnd:
        print(position)
        position = choosePath(matrix, pheromoneMatrix, position, randomRange)
        path.append(position)
        costPath = costPath + matrix[position[0]][position[1]]
        if position == end:
            atEnd = True
    print(path)
    print(costPath)
    return path, costPath


def choosePath(matrix, pheromoneMatrix, position, randomRange):
    #check if we are on a border
    print(len(matrix))
    if position[0] == len(matrix) - 1:
        return [position[0], position[1] + 1]
    if position[1] == len(matrix) - 1:
        return [position[0] + 1, position[1]]
    # Check which number is higher + some randomness for funsies
    pHor = pheromoneMatrix[position[0]][position[1] + 1]
    pVer = pheromoneMatrix[position[0] + 1][position[1]]
    pTotal = pHor + pVer
    randomN = random.randrange(0, 100)/100
    if pHor == 0:
        pHor = 0.5
    if pVer == 0:
        pVer = 0.5
    if pTotal == 0:
        pTotal = 1
        randomN = random.randrange(0, 100)/100
    print("random numbers", randomN)
    print("horz", pHor / pTotal)
    if pHor / pTotal > randomN:
        return [position[0], position[1] + 1]
    else:
        return [position[0] + 1, position[1]]

def makeEmptyMatrix(l, w):
    m = []
    for i in range(l) :
        m.append([0] * w)
    return m



def getShortestRoute(matrix):
    route = getStraightDiagonal(matrix)
    pheromoneMatrix = makeEmptyMatrix(len(matrix), len(matrix[0]))
    print(pheromoneMatrix)
    shortest = 9999999999999999999999999999
    shortestRoute = []
    #elts do it like antsssss
    shortRouteFound = False
    randomRange = 20
    while randomRange > 0:
        routes = []
        distances = []

        allSame = True
    #first we make 10 ants that are going to walk the route
        for i in range(0, 200):
            #what is an eant? basically a random path selector at this point, later it will be more likely to choose the short path
            print("Ant ", i)
            route, costPath = ant(matrix, pheromoneMatrix, randomRange)
            routes.append(route)
            distances.append(costPath)
            if costPath < shortest:
                allSame = False
                shortest = costPath
                shortestRoute = route
        #Update the pheronomes
        print("______")
        print(pheromoneMatrix)
        nMatrix = []
        for line in pheromoneMatrix:
            nLine = [i * 0.5 for i in line]
            nMatrix.append(nLine)
        pheromoneMatrix = nMatrix
        print(pheromoneMatrix)
        for j in range(0, len(distances)):
             distance = distances[j]
             route = routes[j]
             print(routes)
             print(pheromoneMatrix)
             for p in route:
                pheromoneMatrix[p[0]][p[1]] = pheromoneMatrix[p[0]][p[1]] + 1/distance
        randomRange = int(randomRange - 1)
        print("randomRange: ", randomRange)
        print(pheromoneMatrix)
        print(shortestRoute)
    return shortest


matrix = loadfile("test.txt")
print(matrix)

shortestRoute = getShortestRoute(matrix)
print("Opdracht 15a: ", shortestRoute)

print("Opdracht 15b: ", shortestRoute)