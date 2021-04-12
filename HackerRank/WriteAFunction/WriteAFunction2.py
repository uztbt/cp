def is_leap(year: int) -> bool:
  if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    return True
  return False