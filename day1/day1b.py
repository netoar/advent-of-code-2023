file_path = "calibration.txt"  # file path
with open(file_path, 'r') as file:
    calibrationList = []
    calibrationCode = 0
    calibrationString = ""
    totalRowLength = 0
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

    for i in calibrationList:
        calibrationCode += i

    print(calibrationCode)
