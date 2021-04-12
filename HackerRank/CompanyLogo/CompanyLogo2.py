from collections import Counter

def companyLogo(s: str) -> list:
  counter = Counter(s)
  return sorted(
    counter.items(),
    key= lambda tpl: (-tpl[1], ord(tpl[0]))
    )[:3]
