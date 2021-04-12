from types import FrameType
from Dijkstra import Graph
import pytest

@pytest.mark.parametrize("v,e,s,t,want", [
  (
    set(['A', 'B', 'C', 'D', 'E', 'F']),
    {
      'A': {'B': 4, 'C': 8},
      'B': {'D': 3, 'E': 8},
      'C': {'D': 1},
      'D': {'F': 10},
      'E': {'F': 9},
      'F': {}
    },
    'A', 'F', 17)
  ])

def test(v:set[str], e: dict[dict[str, int]], s: str, t :str, want: int):
  graph = Graph(v, e)
  assert graph.dijkstra(s, t) == want