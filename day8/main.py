def loadfile(name):
    input = []
    output = []
    lines = []
    f = open(name, "r")
    for x in f:
        if x.endswith('\n'):
            x = x[:-1]
        lines.append(x)
        beforeLine = True
        outputline = []
        inputline = []
        for value in x.split(" "):
            if value == "|":
                beforeLine = False
            elif beforeLine == False:
                outputline.append(value)
            else:
                inputline.append(value)
        input.append(inputline)
        output.append(outputline)
    return [lines, input, output]

def findEasyNumbers(output):
    counter = 0
    for line in output:
        for value in line:
            if len(value) == 2 or len(value) == 4 or len(value) == 7 or len(value) == 3:
                counter += 1
    return counter

def findTranslation(line):
    #Normal = [a,b,c,d,e,f,g]
    translation = ["","","","","","",""]
    basic = "abcdefg"
    number1 = ""
    number4 = ""
    number7 = ""
    #find easy numbers
    for value in line.split(" "):
        if len(value) == 2:
            number1 = ''.join(sorted(value))
        elif len(value) == 3:
            number7 = ''.join(sorted(value))
        elif len(value) == 4:
            number4 =''.join(sorted(value))
    #find a
    if number1 == number7[:2]:
        translation[0] = number7[2]
    elif number1 == number7[1:]:
        translation[0] = number7[0]
    else:
        translation[0] = number7[1]
    #cf 25
    cf = number1
    #bd 13
    bd = number4.replace(number1[0],"").replace(number1[1],"")

    #find the 6 to figure out c/f, only 6len with no c
    numbersLen6 = getOptionsSpecificLen(line, 6)
    print(numbersLen6)
    for number in numbersLen6:
        if str(number).find(cf[0])==-1:
            translation[2] = cf[0]
            translation[5] = cf[1]
        elif str(number) .find(cf[1])==-1:
            translation[2] = cf[1]
            translation[5] = cf[0]
    #find the 0 to figure out bd
        elif str(number).find(bd[0])==-1:
            translation[3] = bd[0]
            translation[1] = bd[1]
        elif str(number).find(bd[1])==-1:
            translation[3] = bd[1]
            translation[1] = bd[0]
    # find the 9 to figure out eg
        else:
            number9 = number
    ge = []
    for character in basic:
        if character not in translation:
            ge.append(character)
    if str(number9).find(ge[0])==-1:
        translation[4] = ge[0]
        translation[6] = ge[1]
    elif str(number9).find(ge[1])==-1:
        translation[4] = ge[1]
        translation[6] = ge[0]

    print(translation)
    return translation


def getOptionsSpecificLen(line, length):
    options = []
    for value in line.split(" "):
        if len(value) == length:
            options.append(''.join(sorted(value)))
    return list(dict.fromkeys(options))


def findAllNumbers(lines, output):
    numbers = []
    translations = []
    counter = 0
    for line in lines:
        result = ""
        translation = findTranslation(line)
        translations.append(translation)
        for number in output[counter]:
            result += str(translate(translation, number))
        print("output: ", output)
        numbers.append(int(result))
        counter += 1
    print(numbers)
    return sum(numbers)

trans = {
    "012456":0,
    "25":1,
    "02346":2,
    "02356":3,
    "1235":4,
    "01356":5,
    "013456":6,
    "025":7,
    "0123456":8,
    "012356":9
}
def translate(translation, number):
    result = 0
    sequence = ""
    translation = "".join(translation)
    for character in number:
        sequence += str(translation.find(character))
    #print("seg", sequence)
    if ''.join(sorted(sequence)) in trans:
        result = trans[''.join(sorted(sequence))]
    else:
        print("Translation: ",translation)
        print("Error", ''.join(sorted(sequence)))
    #print("res", result)
    return result

[lines, input, output] = loadfile("day8/data.txt")
result = findEasyNumbers(output)
result2 = findAllNumbers(lines, output)



print("solution day8a: " + str(result))
print("solution day8b: " + str(result2))