import sys
'''
  Referencias utilizadas:
  https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/
'''

# Obtener el path del grafo y lo convierte
# a un array [[v11, v12, w], ..., [vm1, vm2, wm]]
def read_document(path):
  with open(path, 'r') as graph:
    count_nodes = int(graph.readline())
    count_edges = int(graph.readline())
    edges = {}
    states = []
    for edge in graph:
      try:
        x = edge.split()
        if (x[0] not in list(edges.keys())): edges[x[0]] = []
        if (x[1] not in list(edges.keys())): edges[x[1]] = []
        edges[x[0]].append((x[1], int(x[2])))
      except:
        states.append(str(int(edge)))
    return count_nodes, count_edges, edges, states

# Clase grafo
class Graph(object):

  def __init__(self, document_name):
    rsc = read_document(document_name)
    self.node_len = rsc[0]
    self.edges_len = rsc[1] 
    self.nodes = list(rsc[2].keys())
    self.edges = rsc[2]
    self.Graph = [ [float('inf') for _ in range(self.node_len)] for _ in range(self.node_len) ]
    
    for node in self.nodes:
      for edge in self.edges[node]:
        self.Graph[self.nodes.index(node)][self.nodes.index(edge[0])] = edge[1]
    
    self.start = rsc[3][0]
    self.finish = rsc[3][1]

  def min_distance(self, distances, queue):
    minimum = float('inf')
    min_index = -1

    for i in range(len(distances)):
      if distances[i] < minimum and i in queue:
        minimum = distances[i]
        min_index = i
    return min_index

  def print_path(self, paths, j): 
    if paths[j] == -1:
      print(self.nodes[j], end=" ")
      return
    self.print_path(paths, paths[j])
    print(self.nodes[j], end=" ")

  def print_solution(self, distances, paths, s0, sf):
    print("Vertex \t\tDistance from Source\tPath")
    for i in range(len(distances)):
      if (sf != self.nodes[i]): continue
      print("%s --> %s \t\t%d \t\t" % (s0, self.nodes[i], distances[i]), end=" ")
      self.print_path(paths, i)

  def shortest_path(self):
    # Indicando el inicio y el final
    s0 = self.start
    sf = self.finish

    # Distancias desde el origen hasta el destino
    distances = [float('inf')] * self.node_len
    distances[self.nodes.index(s0)] = 0

    # Array de movimientos
    paths = [-1] * self.node_len
    queue = [i for i in range(self.node_len)]
    
    while queue:
      u = self.min_distance(distances , queue)
      queue.remove(u)

      for i in range(self.node_len):
        if self.Graph[u][i] and (i in queue) and (distances[u] + self.Graph[u][i] < distances[i]):
          distances[i] = distances[u] + self.Graph[u][i]
          paths[i] = u
    self.print_solution(distances, paths, s0, sf)

if __name__ == "__main__":
    path = sys.argv[1]
    graph = Graph(path)
    graph.shortest_path()