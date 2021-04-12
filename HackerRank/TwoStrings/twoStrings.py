#!/bin/python3


def twoStrings(s1: str, s2: str):
    if frozenset(s1) & frozenset(s2) == frozenset([]):
        return "NO"
    else:
        return "YES"
