#!/bin/python3
from typing import List


def maximumToys(prices: List[int], k: int):
    ans = 0
    prices.sort(reverse=True)
    while prices != []:
        cheapest = prices.pop()
        if cheapest <= k:
            ans += 1
            k -= cheapest
        else:
            break
    return ans

if __name__ == "__main__":
