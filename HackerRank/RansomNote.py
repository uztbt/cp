#!/bin/python3

from typing import List


class ZDic(dict):
    def __missing__(self, key):
        return 0


def checkMagazine(magazine: List[str], note: List[str]):
    zdicMagazine = ZDic()
    for w in magazine:
        zdicMagazine[w] += 1
    for w in note:
        zdicMagazine[w] -= 1
        if zdicMagazine[w] < 0:
            print("No")
            return
    print("Yes")
