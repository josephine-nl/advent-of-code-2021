def loadfile(name):
    lines = []
    f = open(name, "r")
    for x in f:
        if x.endswith('\n'):
            x = x[:-1]
        lines.append(x.split("-"))
    return lines


def pathFromPosition (position, graph, path, s, e, goingTwice, bt):
    beenThere = bt.copy()
    path = path + "-" + position
    print(path)
    paths = []
    if position == e:
        return [path]
    else:
        edges = findEdgesFromPosition(position, graph)
        if len(edges) == 0:
            print("Doodlopend ", path)
            return []
        for edge in edges:
            if not position[0].isupper():
                if goingTwice == False:
                    graph = removeNodeFromGraph(graph, position)
                else:
                    if position == s:
                        graph = removeNodeFromGraph(graph, position)
                    elif position in beenThere:
                        print(beenThere)
                        print("hiephoooi", path)
                        goingTwice = False
                        for p in beenThere:
                            graph = removeNodeFromGraph(graph, p)
                    else:
                        beenThere.append(position)
                        print("Beenthere", position, path)
            cedge = edge.copy()
            cedge.remove(position)
            nextNode = cedge[0]
            print(goingTwice)
            paths.extend(pathFromPosition(nextNode, graph, path, s, e, goingTwice, beenThere))
    return paths

def removeNodeFromGraph (graph, position):
    g = []
    for edge in graph:
        if position not in edge:
            g.append(edge)
    return g

def findEdgesFromPosition (position, graph):
    edges = []
    for edge in graph:
        if position in edge:
            edges.append(edge)
    return edges



originalGraph = loadfile("test.txt")
print(originalGraph)
endPaths = pathFromPosition("start", originalGraph, "", "start", "end", False, [])
endPaths2 = pathFromPosition("start", originalGraph, "", "start", "end", True, [])
print(endPaths)
print(endPaths2)
endPaths2 = list(dict.fromkeys(endPaths2))
print("Opdracht 12a: ", len(endPaths))

print("Opdracht 12b: ", len(endPaths2))