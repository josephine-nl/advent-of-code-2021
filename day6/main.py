def loadfile(name):
    fishies = {}
    f = open(name, "r")
    for x in f:
        for number in x.split(","):
            number = int(number)
            if number in fishies:
                fishies[number] = fishies[number] + 1
            else:
                fishies[number] = 1
    return fishies


def FishSimulation(fishies, numberOfDays, startReproduce, betweenReproduce):
    for day in range(1, numberOfDays + 1):
        nextdayFishies = {}
        print("Day: ", day)
        for timeframe, amount in fishies.items():
            if timeframe == 0:
                #new fishies
                nextdayFishies[startReproduce] = amount

                if betweenReproduce in nextdayFishies:
                    nextdayFishies[betweenReproduce] = nextdayFishies[betweenReproduce] + amount
                else:
                    nextdayFishies[betweenReproduce] = amount
            else:
                if timeframe - 1 in nextdayFishies:
                    nextdayFishies[timeframe - 1] = nextdayFishies[timeframe - 1] + amount
                else:
                    nextdayFishies[timeframe - 1] = amount
        print(fishies)
        fishies = nextdayFishies.copy()
    return(fishies)


def getAmount(fishies):
    totalAmount = 0
    for timeframe, amount in fishies.items():
        totalAmount = totalAmount + amount
    return totalAmount


fishies = loadfile("day6/data.txt")

print(fishies)
fishies = FishSimulation(fishies, 256, 8, 6)
print("Amount of fish: ", getAmount(fishies))
