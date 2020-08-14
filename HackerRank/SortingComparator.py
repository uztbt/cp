from functools import cmp_to_key


class Player:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    # def __repr__(self):

    def comparator(a, b):
        ans = 0
        if a.score > b.score:
            ans = -1
        elif a.score < b.score:
            ans = 1
        else:
            if a.name < b.name:
                ans = -1
            elif a.name > b.name:
                ans = 1
            else:
                ans = 0
        return ans


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
