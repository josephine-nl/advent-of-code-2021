def loadfile(name):
    values = []
    f = open(name, "r")
    for x in f:
        if x.endswith('\n'):
            x = x[:-1]
        values.append(x)
    return values


def calculateRates (values):
    gamma = ""
    epsilon = ""
    for i in range(0, len(values[0])):
        valuez0 = []
        valuez1 = []
        for value in values:
            print(value[i])
            if value[i] == "0":
                valuez0.append(value)
            else:
                valuez1.append(value)
        if len(valuez1) > len(valuez0):
            gamma += "1"
            epsilon += "0"
        elif len(valuez1) < len(valuez0):
            gamma += "0"
            epsilon += "1"
        else:
            print("ERROr")
    return [gamma, epsilon]


def calculateRatings(type, values):
    valuez = values.copy()
    position = 0
    while len(valuez) > 1:
        valuez0 = []
        valuez1 = []
        for value in valuez:
            print(value[position])
            if value[position] == "0":
                valuez0.append(value)
            else:
                valuez1.append(value)
        if type == "oxygen generator rating":
            print(type)
            print(valuez1)
            if len(valuez1) > len(valuez0):
                valuez = valuez1.copy()
            elif len(valuez1) < len(valuez0):
                valuez = valuez0.copy()
            else:
                valuez = valuez1.copy()
        elif type == "CO2 scrubber rating":
            if len(valuez1) < len(valuez0):
                valuez = valuez1.copy()
            elif len(valuez1) > len(valuez0):
                valuez = valuez0.copy()
            else:
                valuez = valuez0.copy()
        position += 1
    return valuez[0]


values = loadfile("data.txt")
[gamma, epsilon] = calculateRates(values)
ogr = calculateRatings("oxygen generator rating", values)
csr = calculateRatings("CO2 scrubber rating", values)

print("gamma rate: ", gamma)
print("epsilon rate: ", epsilon)
print("oxygen generator rating: ", ogr)
print("CO2 scrubber rating: ", csr)

print("solution day3a: " + str(int(gamma, 2) * int(epsilon, 2)))
print("solution day3b: " + str(int(ogr, 2) * int(csr, 2)))