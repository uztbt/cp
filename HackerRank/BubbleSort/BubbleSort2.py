from array import array

def countSwaps(arr: array):
  numSwaps = 0
  n = len(arr)
  for i in range(n):
    for j in range(n-i-1):
      if arr[j] > arr[j+1]:
        tmp = arr[j+1]
        arr[j+1] = arr[j]
        arr[j] = tmp
        numSwaps += 1
  print(
    f"""Array is sorted in {numSwaps} swaps.
First Element: {arr[0]}
Last Element: {arr[-1]}"""
  )
    