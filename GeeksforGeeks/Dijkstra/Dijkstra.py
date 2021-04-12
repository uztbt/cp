class Graph:
  def __init__(self, V: set[str], E: dict[dict[str, int]]) -> None:
      super().__init__()
      self.V = V
      self.E = E
  
  def dijkstra(self, s: str, t: str) -> int:
    """
    Returns the shortest path from s to t
    """
    Dist = dict()
    for vertex in self.V:
      Dist[vertex] = 10 ** 9
    Dist[s] = 0
    SptSet = set()
    while SptSet != self.V:
      u = closest(Dist, self.V.difference(SptSet))
      SptSet.add(u)
      EdgeFromU = self.E[u]
      Adjacents = set(EdgeFromU.keys()).difference(SptSet)
      for adj in Adjacents:
        Dist[adj] = min(Dist[adj], Dist[u] + EdgeFromU[adj])
    return Dist[t]
  
def closest(Dist: dict[str, int], cands: set[str]) -> str:
  try:
    ret = cands.pop()
  except KeyError:
    raise RuntimeError("This won't happen!")
  for cand in cands:
    if Dist[cand] < Dist[ret]:
      ret = cand
  return ret
