def normalize(string: str):
    result = ""
    for letter in string:
        if letter not in result:
            result += letter
    return result


def mtt(string: str, k):
    blocks = len(string) // k
    for i in range(blocks):
        offset = i * k
        ui = string[offset : offset + k]
        ti = normalize(ui)
        print(ti)


if __name__ == "__main__":
    string = input()
    k = int(input())
    mtt(string, k)
