file_path = "calibration.txt"  # file path
with open(file_path, 'r') as fileRaw:
    calibrationList = []
    calibrationCode = 0
    calibrationString = ""
    file = []
    newLine = ""
    resultDictionary = {}
    totalRowLength = 0

    numberToDigit = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    for lineRaw in fileRaw:
        # Iterate through the text
        i = 0
        newLine = ""
        while i < len(lineRaw):
            # Try to find the first matching word from the dictionary
            found = False
            for word in numberToDigit.keys():
                if lineRaw[i:].startswith(word):
                    # Append the corresponding number to the result
                    newLine += numberToDigit[word]
                    # Move the index to the end of the matched word
                    i += len(word)
                    found = True
                    break
            if not found:
                # If no match is found, append the current character as is
                newLine += lineRaw[i]
                i += 1

            numbersInRow = []
            for char in newLine:
                if char.isdigit():
                    # add it into the list
                    numbersInRow.append(char)
                else:
                    continue

            rowLength = len(numbersInRow)
            totalRowLength += rowLength

            if rowLength > 1:
                calibrationString = str(numbersInRow[0]) + str(numbersInRow[rowLength - 1])
            else:
                calibrationString = str(numbersInRow[0]) + str(numbersInRow[0])

            calibrationNumber = int(calibrationString)
            calibrationList.append(calibrationNumber)

        print(newLine.strip(), lineRaw.strip(), calibrationNumber)

    for line in file:
        # print(line)
        numbersInRow = []
        for char in line:
            if char.isdigit():
                # add it into the list
                numbersInRow.append(char)
            else:
                continue

        rowLength = len(numbersInRow)
        totalRowLength += rowLength

        if rowLength > 1:
            calibrationString = str(numbersInRow[0]) + str(numbersInRow[rowLength - 1])
        else:
            calibrationString = str(numbersInRow[0]) + str(numbersInRow[0])

        calibrationNumber = int(calibrationString)
        calibrationList.append(calibrationNumber)

    # print(resultDictionary)
    for i in calibrationList:
        calibrationCode += i

    # print(calibrationCode)
