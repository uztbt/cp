def getMin(string: str):
    ins, acc = 0, 0
    for p in string:
        if p == "(":
            acc += 1
        else:
            acc -= 1
        if acc == -1:
            ins += 1
            acc = 0
    return ins + acc
