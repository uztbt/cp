from typing import List


def quicksort(arr: List[int])->List[int]:
  l = len(arr)
  if l == 0:
    return []
  elif l == 1:
    return arr
  else:
    pivot = arr.pop(0)
    former = []
    latter = []
    for item in arr:
      if item < pivot:
        former.append(item)
      else:
        latter.append(item)
    return quicksort(former) + [pivot] + quicksort(latter)

def quicksortMutating(arr: List[int], low: int, high: int):
  if low < high:
    pivot = arr.pop(low)
    former = []
    latter = []
    for item in arr[low:high+1]:
      if item < pivot:
        former.append(item)
      else:
        latter.append(item)
    pivotIndex = len(former) + low
    arr[low:pivotIndex] = former
    arr[pivotIndex] = pivot
    arr[pivotIndex+1:high+1] = latter
    print(arr)
    quicksortMutating(arr, low, pivotIndex - 1)
    quicksortMutating(arr, pivotIndex + 1, high)

if __name__ == "__main__":
  arr = [3, 1, 8, 6, 9, 3, 5, 2]
  arr2 = arr.copy()
  print(f"Soted arr: {quicksort(arr)}")
  quicksortMutating(arr2, 0, len(arr2) - 1)
  print(f"Soted arr2: {arr2}")