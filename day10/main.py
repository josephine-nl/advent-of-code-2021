def loadfile(name):
    lines = []
    f = open(name, "r")
    for x in f:
        if x.endswith('\n'):
            x = x[:-1]
        lines.append(x)
    return lines

def findCorrupted(line):
    closingsExpected = []
    for character in line:
        if character in openingCharacters.keys():
            closingsExpected.insert(0,openingCharacters[character])
        elif character == closingsExpected[0]:
            del closingsExpected[0]
        else:
            return closingCharacters[character]
    return 0

def completeLine(line):
    closingsExpected = []
    total = 0
    for character in line:
        if character in openingCharacters.keys():
            closingsExpected.insert(0,openingCharacters[character])
        elif character == closingsExpected[0]:
            del closingsExpected[0]
        else:
            return 0
    for character in closingsExpected:
        total = (total*5) + closingCharactersComplete[character]
    return total

openingCharacters = {
    "(":")",
    "<":">",
    "{":"}",
    "[":"]"
}
closingCharacters = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
closingCharactersComplete = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

lines = loadfile("data.txt")
print(lines)
total = 0
for line in lines:
    total = total + findCorrupted(line)
print("Answer 10a: ", total)
total = 0
scores = []
for line in lines:
    score = completeLine(line)
    if score > 0:
        scores.append(score)

scores = sorted(scores)
middlescore = scores[int(len(scores)/2-0.5)]
print("Answer 10b: ", middlescore)