# 12 red cubes, 13 green cubes, and 14 blue cubes
file_path = "game.txt"  # file path
desiredGame = {
    "red": 12,
    "green": 13,
    "blue": 14
}

print("hello this is the advent code day 2")
gameList = []
number = ""
color = ""
result = 0
total = 0
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
with open(file_path, 'r') as fileRaw:
    for file in fileRaw:
        gameInfoList = file.split(":")
        # print(gameInfoList)
        # ["Game 1", "3 blue, 4 red; 1 red, 2 green, 2 blue; 2 green]
        gameDetails = gameInfoList[1].split(";")
        # print(gameDetails)
        # ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"]
        numberOfGames = len(gameDetails)
        validGame = True
        for currentGame in gameDetails:
            # print(currentGame)
            currentGameDetails = currentGame.split(",")
            # print(currentGameDetails)
            # ["3 blue", "4 red"]
            attemptGame = {}
            for colors in currentGameDetails:
                # print(colors)
                color = ""
                number = ""
                for char in colors:
                    if char.isdigit():
                        number += char
                    else:
                        color += char
                attemptGame[color.strip()] = int(number)

            # check if game is valid
            # print(attemptGame)
            # print(desiredGame)

            for key in desiredGame:
                if key in attemptGame:
                    if desiredGame[key] < attemptGame[key]:
                        # print(desiredGame[key], "and", type(attemptGame[key]))
                        validGame = False
                        break
                else:
                    validGame = True
            # print(validGame)

            if validGame == False:
                break

        if validGame == True:
            gameList.append(gameInfoList[0])
            print(gameList)
            for char in gameInfoList[0]:
                if char.isdigit():
                    result = result * 10 + int(char)
                    print(result)
                    # result += int(char)
            total += result
            print(total)
        result = 0
    print(total)
