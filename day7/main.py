def loadfile(name):
    numbers = []
    f = open(name, "r")
    for x in f:
        for number in x.split(","):
            number = int(number)
            numbers.append(number)
    return numbers

def caculateTravelLinear(numbers, endpoint):
    travel = 0
    for number in numbers:
        distance = endpoint - number if (endpoint - number) > 0 else (endpoint - number) * -1
        travel = travel + distance
    return travel

def caculateTravelFuel(numbers, endpoint):
    travel = 0
    for number in numbers:
        distance = endpoint - number if (endpoint - number) > 0 else (endpoint - number) * -1
        rangeOfNumber = range(0, distance + 1)
        fuel = sum(rangeOfNumber)
        travel = travel + fuel
    return travel

def findLowestTravel(function, numbers):
    median = int(numbers[int(len(numbers) / 2)] if len(numbers) % 2 == 0 else (numbers[int(len(numbers) / 2 - 1)] + (numbers[int(len(numbers) / 2 + 1)])/2))
    average = round(sum(numbers)/len(numbers))
    print("Median: " + str(median))
    print("Average: " + str(average))

    lowestTravel = 99999999999999999999999999999999999999999999999999999999999999999999999999999
    rangeOfLoop = range(median, average + 1) if median < average + 1 else range(average - 1, median + 1)
    for endpoint in rangeOfLoop:
        travel = function(numbers, endpoint)
        print("Endpoint: ", str(endpoint) + "Travel: ", str(travel) + "-")
        if travel < lowestTravel:
            lowestTravel = travel
            print("Lowest: ", travel)
    return lowestTravel

numbers = sorted(loadfile("data.txt"))
lowestTravelA = findLowestTravel(caculateTravelLinear, numbers)
lowestTravelB = findLowestTravel(caculateTravelFuel, numbers)

print("solution day7a: " + str(lowestTravelA))
print("solution day7b: " + str(lowestTravelB))
