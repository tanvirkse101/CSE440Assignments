import itertools


def draw(player, x):
    control = 0

    # North
    if x[4] == "N":
        nn = int(alphabet.index(x[2]))
        a[((number.index(x[0]) * 3)) - 1][4 * nn + 2] = ("_")
        a[((number.index(x[0]) * 3)) - 1][4 * nn + 3] = ("_")
        a[((number.index(x[0]) * 3)) - 1][4 * nn + 4] = ("_")

        if a[3 * int(x[0]) - 1][(alphabet.index(x[2]) * 4) + 3] != ' ' and a[3 * int(x[0]) - 4][
            (alphabet.index(x[2]) * 4) + 3] != ' ' and a[3 * int(x[0]) - 2][
            (alphabet.index(x[2]) * 4) + 5] != ' ' and a[3 * int(x[0]) - 2][
            (alphabet.index(x[2]) * 4) + 1] != ' ':
            a[3 * int(x[0]) - 2][(alphabet.index(x[2]) * 4) + 3] = player
            control = 1

        if a[3 * (int(x[0]) - 1) - 1][(alphabet.index(x[2]) * 4) + 3] != ' ' and a[3 * (int(x[0]) - 1) - 4][
            (alphabet.index(x[2]) * 4) + 3] != ' ' and a[3 * (int(x[0]) - 1) - 2][
            (alphabet.index(x[2]) * 4) + 5] != ' ' and a[3 * (int(x[0]) - 1) - 2][
            (alphabet.index(x[2]) * 4) + 1] != ' ':
            a[3 * (int(x[0]) - 1) - 2][(alphabet.index(x[2]) * 4) + 3] = player
            control = 1

        if control == 1:
            player = players[players.index(player) - 1]

    # South
    if x[4] == "S":
        ss = int(alphabet.index(x[2]))
        a[((number.index(x[0]) * 3)) + 2][4 * ss + 2] = ("_")
        a[((number.index(x[0]) * 3)) + 2][4 * ss + 3] = ("_")
        a[((number.index(x[0]) * 3)) + 2][4 * ss + 4] = ("_")

        if a[3 * int(x[0]) - 1][(alphabet.index(x[2]) * 4) + 3] != ' ' and a[3 * int(x[0]) - 4][
            (alphabet.index(x[2]) * 4) + 3] != ' ' and a[3 * int(x[0]) - 2][
            (alphabet.index(x[2]) * 4) + 5] != ' ' and a[3 * int(x[0]) - 2][
            (alphabet.index(x[2]) * 4) + 1] != ' ':
            a[3 * int(x[0]) - 2][(alphabet.index(x[2]) * 4) + 3] = player
            control = 1

        if a[3 * (int(x[0]) + 1) - 1][(alphabet.index(x[2]) * 4) + 3] != ' ' and a[3 * (int(x[0]) + 1) - 4][
            (alphabet.index(x[2]) * 4) + 3] != ' ' and a[3 * (int(x[0]) + 1) - 2][
            (alphabet.index(x[2]) * 4) + 5] != ' ' and a[3 * (int(x[0]) + 1) - 2][
            (alphabet.index(x[2]) * 4) + 1] != ' ':
            a[3 * (int(x[0]) + 1) - 2][(alphabet.index(x[2]) * 4) + 3] = player
            control = 1

        if control == 1:
            player = players[players.index(player) - 1]

    # East
    if x[4] == "E":
        ee = int(x[0])
        a[3 * ee - 1][(alphabet.index(x[2]) * 4) + 5] = ("|")
        a[3 * ee - 2][(alphabet.index(x[2]) * 4) + 5] = ("|")
        a[3 * ee - 3][(alphabet.index(x[2]) * 4) + 5] = ("|")

        if a[3 * int(x[0]) - 1][(alphabet.index(x[2]) * 4) + 3] != ' ' and a[3 * int(x[0]) - 4][
            (alphabet.index(x[2]) * 4) + 3] != ' ' and a[3 * int(x[0]) - 2][
            (alphabet.index(x[2]) * 4) + 5] != ' ' and a[3 * int(x[0]) - 2][
            (alphabet.index(x[2]) * 4) + 1] != ' ':
            a[3 * int(x[0]) - 2][(alphabet.index(x[2]) * 4) + 3] = player
            control = 1

        if a[3 * int(x[0]) - 1][((alphabet.index(x[2]) + 1) * 4) + 3] != ' ' and a[3 * int(x[0]) - 4][
            ((alphabet.index(x[2]) + 1) * 4) + 3] != ' ' and a[3 * int(x[0]) - 2][
            ((alphabet.index(x[2]) + 1) * 4) + 5] != ' ' and a[3 * int(x[0]) - 2][
            ((alphabet.index(x[2]) + 1) * 4) + 1] != ' ':
            a[3 * int(x[0]) - 2][((alphabet.index(x[2]) + 1) * 4) + 3] = player
            control = 1

        if control == 1:
            player = players[players.index(player) - 1]

    # West
    if x[4] == "W":
        ww = int(x[0])
        a[3 * ww - 1][(alphabet.index(x[2]) * 4) + 1] = ("|")
        a[3 * ww - 2][(alphabet.index(x[2]) * 4) + 1] = ("|")
        a[3 * ww - 3][(alphabet.index(x[2]) * 4) + 1] = ("|")
        if a[3 * int(x[0]) - 1][(alphabet.index(x[2]) * 4) + 3] != ' ' and a[3 * int(x[0]) - 4][
            (alphabet.index(x[2]) * 4) + 3] != ' ' and a[3 * int(x[0]) - 2][
            (alphabet.index(x[2]) * 4) + 5] != ' ' and a[3 * int(x[0]) - 2][
            (alphabet.index(x[2]) * 4) + 1] != ' ':
            a[3 * int(x[0]) - 2][(alphabet.index(x[2]) * 4) + 3] = player
            control = 1

        if a[3 * int(x[0]) - 1][((alphabet.index(x[2]) - 1) * 4) + 3] != ' ' and a[3 * int(x[0]) - 4][
            ((alphabet.index(x[2]) - 1) * 4) + 3] != ' ' and a[3 * int(x[0]) - 2][
            ((alphabet.index(x[2]) - 1) * 4) + 5] != ' ' and a[3 * int(x[0]) - 2][
            ((alphabet.index(x[2]) - 1) * 4) + 1] != ' ':
            a[3 * int(x[0]) - 2][((alphabet.index(x[2]) - 1) * 4) + 3] = player
            control = 1

        if control == 1:
            player = players[players.index(player) - 1]

    for g in range(2, (column * 7) - 1, 4):
        a[(row * 3) - 1][g:g + 3] = ('___')

    rowStart = 1
    for w in range(1, (row * 3), 3):
        a[w][0] = (rowStart)
        rowStart += 1

    for i in range(row * 3):
        a[i][1] = '|'
        if i == 0:
            print("   ", end="")
            for s in range(column):
                print(alphabet[s], "   ", end="", sep="")
            print()

            print("  ___", end="")
            for s in range(column - 2):
                print(" ___", end="")
            print(" ___")
        for j in range((column) * 5 - (column - 2)):
            a[i][((column) * 5 - (column - 2)) - 1] = '|'
            print(a[i][j], sep='', end="")
        print()

    if player == players[int(players.index(player))]:
        player = players[int(players.index(player)) - 1]
        return player


play = 'y'
while play in {'y', 'Y'}:
    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    direction = ["N", "S", "E", "W"]

    firstPlayer = input("Enter a character for first player: ")
    while not firstPlayer.__len__() == 1:
        firstPlayer = input("Enter a correct character for first player: ")

    secondPlayer = input("Enter a character for second player: ")
    while not secondPlayer.__len__() == 1:
        secondPlayer = input("Enter a correct character for second player: ")

    players = [firstPlayer, secondPlayer]
    player = players[0]

    row = input("Enter row count [3-9]: ")
    while not row.isdigit() or int(row) not in range(3, 10):
        row = input("Enter correct row count [3-7]: ")
    row = int(row)

    column = input("Enter column count [3-25]: ")
    while not column.isdigit() or int(column) not in range(3, 26):
        column = input("Enter correct column count [3-19]: ")
    column = int(column)

    a = [[' ' for _ in range(column * 7)] for _ in range(row * 3)]

    for g in range(2, (column * 7) - 1, 4):
        a[(row * 3) - 1][g:g + 3] = ('___')

    rowStart = 1
    for w in range(1, (row * 3), 3):
        a[w][0] = (rowStart)
        rowStart += 1

    for i in range(row * 3):
        a[i][1] = '|'
        if i == 0:
            print("   ", end="")
            for s in range(column):
                print(alphabet[s], "   ", end="", sep="")
            print()

            print("  ___", end="")
            for s in range(column - 2):
                print(" ___", end="")
            print(" ___")
        for j in range((column) * 5 - (column - 2)):
            a[i][((column) * 5 - (column - 2)) - 1] = '|'
            print(a[i][j], sep='', end="")
        print()

    combination = list(itertools.product(number[0:column], alphabet[0:column], direction))
    for i in range(column):
        combination.remove(("1", alphabet[i], "N"))
        combination.remove((number[row - 1], alphabet[i], "S"))
    for j in range(row):
        combination.remove((number[j], "A", "W"))
        combination.remove((number[j], alphabet[column - 1], "E"))
   
    print('\nFormat:Row Col Direction(N,S,E,W) \nExample: 1 A S \nExample: 2 B W  \n')

    while combination != []:
        print("Player", str(player), "please enter a coordinate: ", end="")
        x = input().upper()
        while len(x) != 5 or (x[0], x[2], x[4]) not in combination:
            x = input("Please enter a correct coordinate: ").upper()

        combination.remove((x[0], x[2], x[4]))
        if x[4] == "E":
            combination.remove((x[0], alphabet[alphabet.index(x[2]) + 1], "W"))
        if x[4] == "W":
            combination.remove((x[0], alphabet[alphabet.index(x[2]) - 1], "E"))
        if x[4] == "N":
            combination.remove((number[number.index(x[0]) - 1], x[2], "S"))
        if x[4] == "S":
            combination.remove((number[number.index(x[0]) + 1], x[2], "N"))
        player = draw(player, x)

    else:
        firstPlayerPoint = sum(bir.count(firstPlayer) for bir in a)
        secondPlayerPoint = sum(iki.count(secondPlayer) for iki in a)
        print(firstPlayer, ": ", firstPlayerPoint, ' ', secondPlayer, ": ", secondPlayerPoint)
        if firstPlayerPoint > secondPlayerPoint:
            print("Winner", firstPlayer)
        elif secondPlayerPoint > firstPlayerPoint:
            print("Winner", secondPlayer)
        else:
            print("Draw")

        play = input("Do you want to play again (Y/y=yes N/n=no) ?")
        while not play in {'Y', 'y', 'N', 'n'}:
            play = input("Do you want to play again (Y/y) ?")
