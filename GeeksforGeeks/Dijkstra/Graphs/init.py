from graphviz import Digraph

dot = Digraph(
  name="dijkstra_init",
  comment = "Demo of the Dijkstra Algorithm",
  directory="out",
  format="png",
  )
dot.node('A')
dot.node('B')
dot.node('C')
dot.node('D')
dot.node('E')
dot.node('F')

dot.edge('A', 'B', label = '4')
dot.edge('A', 'C', label = '8')
dot.edge('B', 'D', label = '3')
dot.edge('B', 'E', label = '8')
dot.edge('C', 'D', label = '1')
dot.edge('D', 'F', label = '10')
dot.edge('E', 'F', label = '6')

if __name__ == "__main__":
  dot.render()