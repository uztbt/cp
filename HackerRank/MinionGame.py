def minion_game(s):
    point_stuart = 0
    point_kevin = 0

    length = len(s)

    for letter in s:
        pass
        if letter in ["A", "E", "I", "O", "U"]:
            point_kevin += length
        else:
            point_stuart += length
        length -= 1

    if point_stuart > point_kevin:
        print("Stuart", point_stuart)
    elif point_stuart < point_kevin:
        print("Kevin", point_kevin)
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
