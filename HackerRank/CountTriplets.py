import array
from collections import Counter

calc_memo = dict()


def findFirstIndex(pred, lst, length):
    for i in range(length):
        if pred(lst[i]):
            return i
    return None


def calc(j, ks_raw, ks_raw_length):
    memo = calc_memo.get(j)
    if memo is None:
        index = findFirstIndex(lambda x: x > j, ks_raw, ks_raw_length)
        if index is None:
            ans = 0
        else:
            ans = ks_raw_length - index
        calc_memo[j] = ans
        return ans
    else:
        return memo


big_calc_memo = dict()


def bigCalc(js, iss, iss_length):
    if js == [] or iss_length == 0:
        return 0
    j, *rest = js
    memo = big_calc_memo.get(j)
    if memo is not None:
        return memo
    else:
        i_start = findFirstIndex(lambda i: i < j, iss, iss_length)
        if i_start is None:
            j_ans = 0
        j_ans = iss_length - i_start
        ans = j_ans + bigCalc(rest, iss[i_start:], iss_length - i_start)
        big_calc_memo[j] = ans
        return ans


# def countTriplets(arr, r):
#     a = array.array("i", arr)
#     d = dict()
#     for i in range(len(a)):
#         if d.get(a[i]) is None:
#             d[a[i]] = [i]
#         else:
#             d[a[i]].append(i)

#     res = 0
#     keys = d.keys()

#     if r == 1:
#         for x in keys:
#             num = len(d[x])
#             res += num * (num - 1) * (num - 2) // 6
#     else:
#         for i_v in keys:
#             js_raw = d.get(i_v * r)
#             ks_raw = d.get(i_v * r * r)
#             if js_raw is None or ks_raw is None:
#                 continue
#             js_raw.reverse()
#             ks_raw.reverse()
#             js_raw_length = len(js_raw)
#             for k in ks_raw:
#                 j_start = findFirstIndex(lambda j: j < k, js_raw, js_raw_length)
#                 if j_start is None:
#                     continue
#                 js = js_raw[j_start:]
#                 iss = list(reversed(d[i_v]))
#                 iss_length = len(iss)
#                 for j in js:
#                     i_start = findFirstIndex(lambda i: i < j, iss, iss_length)
#                     if i_start is None:
#                         continue
#                     res += iss_length - i_start
#                     iss = iss[i_start:]
#                     iss_length -= i_start
#     return res


def countTriplets(arr, r):
    res = 0
    pairs = Counter()
    if r == 1:
        counter = Counter(arr)
        for x in counter:
            num = counter[x]
            res += num * (num - 1) * (num - 2) // 6
        return res
    else:
        counter = Counter()
        for k in arr:
            counter[k] += 1
            j, rem = divmod(k, r)
            if rem != 0:
                continue
            pairs[(j, k)] += counter[j]
            i, rem = divmod(j, r)
            if rem != 0:
                continue
            res += pairs[(i, j)]
        return res


if __name__ == "__main__":
    arr, r = (
        [
            1,
            1000000000,
            100000,
            100,
            100,
            10,
            100,
            1000000000,
            100,
            10000000,
            100000000,
            100000000,
            10000000,
            1,
            1000,
            100000000,
            10000000,
            1000000,
            100,
            1,
            100000,
            10000,
            100000,
            10000,
            10000000,
            10,
            100,
            1000000,
            1000,
            10000,
            10,
            1000000,
            1000,
            1000000000,
            1,
            10000000,
            1,
            10000,
            10000000,
            100,
            10,
            10000000,
            100,
            10,
            10000000,
            100000,
            1000000000,
            10000,
            10000,
            10,
            1000000,
            1000000000,
            10000000,
            10,
            1000000,
            10000,
            100000,
            100000000,
            100,
            100000000,
            10000,
            100000,
            1000000,
            1,
            10000,
            1000000000,
            10000000,
            1000000,
            1000,
            1000000,
            1,
            100000,
            10000,
            1000,
            1000000,
            10,
            1,
            100000,
            100000000,
            10000,
            100000000,
            1000000,
            1000000,
            100000,
            100000000,
            10000,
            10,
            100000,
            100,
            1000,
            1000,
            100000000,
            100000000,
            100,
            100000000,
            1000,
            10,
            1000000,
            10,
            10000,
            10000,
            100,
            10,
            100000000,
            100000,
            10000000,
            100,
            100000,
            10000,
            100,
            1,
            10000,
            100000000,
            100000000,
            1000000000,
            100000000,
            100,
            1,
            1000,
            1000000,
            100000,
            1000000000,
            10000,
            10000,
            10,
            100000,
            1000000000,
            100,
            1000,
            1,
            100000000,
            10000000,
            100,
            1,
            100000000,
            1000000000,
            1000000000,
            100,
            100000,
            1000000,
            1000000,
            10000000,
            100,
            10000,
            100000,
            10000,
            100000,
            10000000,
            10000,
            1,
            1000,
            100,
            1000000000,
            1000000000,
            1000000,
            1,
        ],
        10,
    )
    print(countTriplets(arr, r))
