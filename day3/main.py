def loadfile(name):
    values = []
    f = open(name, "r")
    for x in f:
        if x.endswith('\n'):
            x = x[:-1]
        values.append(x)
    return values

def SumUpBinary(valuez):
    numbers = [0] * len(valuez[0])
    count = 0
    for value in valuez:
        for i in range(0, len(value)):
            numbers[i] += int(value[i])
        count += 1
    return numbers

def SumToNewBinaries(numbers, amount):
    gammaRate = ""
    epsilonRate = ""
    for number in numbers:
        if number > (amount*0.50):
            gammaRate = gammaRate + "1"
            epsilonRate = epsilonRate + "0"
        elif number == (amount*0.50):
            gammaRate = gammaRate + "0"
            epsilonRate = epsilonRate + "1"
        else:
            gammaRate = gammaRate + "0"
            epsilonRate = epsilonRate + "1"
    return [gammaRate, epsilonRate]

def findLifeSupportRating(gammaRate, epsilonRate):
    oList = values.copy()
    cList = values.copy()
    for i in range(0, len(str(gammaRate))):
        oListCopy = oList.copy()
        cListCopy = cList.copy()
        onumbers = SumUpBinary(oListCopy)
        cnumbers = SumUpBinary(cListCopy)
        [gammaRate, ha] = SumToNewBinaries(onumbers, len(oListCopy))
        [ha, epsilonRate] = SumToNewBinaries(cnumbers, len(cListCopy))

        print("copy")
        print(cListCopy)

        for j in range(len(oListCopy) - 1, -1, -1):
            print("c")
            print(gammaRate)
            print(i)
            print(gammaRate[i])

            print(oListCopy[j])
            if not oListCopy[j][i].startswith(gammaRate[i]) and not len(oListCopy) < 3:
                print("delete" + oListCopy[j])
                del oListCopy[j]
            elif (len(oListCopy) == 2) and (int(oListCopy[j][i]) == 0):
                print("delete %" + oListCopy[j])
                del oListCopy[j]
            else:
                print(gammaRate[i])
                print(oListCopy[j][i])
                print( int(oListCopy[j][i]) == int(gammaRate[i]))
                print(not oListCopy[j][i].startswith(gammaRate[i]))
                print(not len(oListCopy) < 2)
                print(oListCopy[j][i] == 0)
                print("PONYBOY")
                print(oListCopy[j])
                print(i)
                print(oListCopy[j][i -1])
                print(len(oListCopy))

        oList = oListCopy.copy()

        for k in range(len(cListCopy) - 1, -1, -1):
            print("h" + str(k))
            print(epsilonRate)
            print(epsilonRate[i])
            print(cListCopy[k][i])
            if not cListCopy[k][i].startswith(epsilonRate[i]) and not len(cListCopy) < 3:
               # print("b")
                del cListCopy[k]
            elif (not cListCopy[k][i].startswith(epsilonRate[i])) and (not len(cListCopy) < 2) and (int(cListCopy[k][i]) == 7):
                print("delete %" + cListCopy[k])
                del cListCopy[k]
            elif (len(cListCopy) == 2) and (int(cListCopy[k][i]) == 7):
                print("delete %" + cListCopy[k])
                del cListCopy[k]
            else:
                print(not cListCopy[k].startswith(gammaRate[:i]))
                print(not len(cListCopy) < 2)
                print(cListCopy[k][i - 1] == 1)
                print("PONYBMAN")
                print(cListCopy[k])
                print(i)
                print(cListCopy[k][i -1])
                print(len(cListCopy))
        cList = cListCopy.copy()

        if len(cListCopy) < 2 and len(oListCopy) < 2:
            print("PRINT")
            print(cListCopy)
            print(oListCopy)
            break
        else:
            print("@@@@@@@@@@@@@@@@@@@@@@")
            print(cList)
            print(oList)
            print("@@@@@@@@@@@@@@@@@@@@@@")
    print("LifeSupport")
    print(len(gammaRate))
    print(oList)
    print(cList)
    return [oList[0],cList[1]]

def BinaryDiagnostic():
    numbers = SumUpBinary(values)
    [gammaRate, epsilonRate] = SumToNewBinaries(numbers, len(values))

    [oxygenGeneratorRating, cO2ScrubberRating] = findLifeSupportRating(gammaRate,epsilonRate)
    print("e:" + epsilonRate)
    print("g:" + gammaRate)
    print("o:" + oxygenGeneratorRating)
    print("c:" + cO2ScrubberRating)
    print("OOO:", int(oxygenGeneratorRating, 2))
    print("CCCC:", int(cO2ScrubberRating, 2))
    return [int(gammaRate, 2) * int(epsilonRate, 2), int(oxygenGeneratorRating, 2) * int(cO2ScrubberRating, 2)]


values = loadfile("data.txt")
print(values)
solution = BinaryDiagnostic()
print("full solution: " + str(solution))
print("solution day3a: " + str(solution[0]))
print("solution day3b: " + str(solution[1]))