import pandas as pd
def loadfile(name):
    lines = []
    f = open(name, "r")
    for x in f:
        lines.append(x)
    return lines

def prepData():
    lines = loadfile("data.txt")
    numbers = lines[0].split(",")
    bingoCards = []
    for i in range(2, len(lines), 6):
        print(lines[i:i+5])
        bingoCard = makeBingoCard(lines[i:i+5])
        bingoCards.append(bingoCard)
    return [numbers, bingoCards]

def makeBingoCard(lines):
    rows = []
    for line in lines:
        row = line.split()
        rows.append(row)
    bingoCard = pd.DataFrame(data=rows, columns=["B", "I", "N", "G", "O"])
    return bingoCard

def printBingoCard(id, BingoCard):
    print("Bingokaart: " + str(id))
    print(BingoCard)
    print()

def checkLine(values):
   checker = 0
   for value in values:
       if value == "x":
           checker += 1
       else:
           break
   #print("Checker:" + str(checker))
   if checker == 5:
        return True
   return False

def checkBingo(id, BingoCard):
    #Vertical Check
    for index, values in BingoCard.iterrows():
        if(checkLine(values)):
            print("WINN:" + str(id))
            return True
    #Horizontal Check
    for index, values in BingoCard.iteritems():
        if(checkLine(values)):
            print("WINN:" + str(id))
            return True
    return False

def signNumberOfBingoCard(id, bingoCard, number):
    for index, values in bingoCard.iteritems():
        for i in range(0, len(values)):
            value = values[i]
            if value == number:
                bingoCard[index][i] = "x"
                print("crossed of: ", number)
                printBingoCard(id, bingoCard)
                return True
    printBingoCard(id, bingoCard)
    return False

def calculateScore(number, bingoCard):
    total = 0
    for index, values in bingoCard.iteritems():
        for i in range(0, len(values)):
            value = values[i]
            if value != "x":
                total += int(value)
    print("Total: ", total)
    print("Number: ", number)
    return int(number)*total

def playingBingo(numbers, bingoCards):
    firstScore = 0
    lastScore = 0
    for number in numbers:
        print(number , " NUMMER: " , number , "!")
        id = 0
        winners = []
        for bingoCard in bingoCards:
            if(signNumberOfBingoCard(id, bingoCard, number)):
                if(checkBingo(id, bingoCard)):
                    print("BINGGOO!")
                    lastScore = calculateScore(number, bingoCard )
                    print("WINNER WINNER CHICKEN DINNER: " + str(lastScore))
                    if(firstScore == 0):
                        firstScore = lastScore
                    winners.append(id)
            id += 1
        # reverse the list to make it easier to pop
        winners = winners[::-1]
        for winner in winners:
            bingoCards.pop(winner)
        if len(bingoCards) == 0:
            break
    print("End of game")
    return [firstScore, lastScore]


[numbers, bingoCards] = prepData()
originalBingoCards = bingoCards.copy()
print(numbers)
print(bingoCards)
[firstScore, lastScore] = playingBingo(numbers, bingoCards)
print("First win " + str(firstScore))
print("Last win " + str(lastScore))