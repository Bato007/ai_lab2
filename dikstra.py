# Obtener el path del grafo y lo convierte
# a un array [[v11, v12, w], ..., [vm1, vm2, wm]]

def read_document(path):
  with open(path, 'r') as graph:
    count_nodes = int(graph.readline())
    count_edges = int(graph.readline())
    edges: Vertex = [[] for _ in range(count_edges)]
    for edge in graph:
      if edge != '\n':
        x = edge.split()
        edges[int(x[0]) -1].append((int(x[1]) -1, int(x[2])))
    return count_nodes, count_edges, edges

# Hace la referencia entre nodos
class Edge(object):
  def __init__(self, s_none, f_none, w_none):
    self.start = s_none
    self.finish = f_none
    self.weight = w_none

# Es el nodo del grafo
class Vertex(object):
  def __init__(self, ref):
    self.node = ref
    self.relations = []

  def create_node(self, f_none, w):
    self.relations.append(Edge(self.node, f_none, w))

  def get_nodes(self):
    return self.relations

  def get_node(self):
    return self.node

# Clase grafo
class Graph(object):

  def __init__(self):
    self.nodes = []
    self.edges = []
    rsc = read_document('exercise1.txt')
    self.node_len = rsc[0]
    self.edges_len = rsc[1] 
    self.edges = rsc[2] #devuelve el array

  def createGraph (self):
    for node in self.edges:
      newNode = Vertex(node)
      for connection in node: #accede a cada uno de los elementos
        newNode.create_node(connection[0], connection[1])
      self.nodes.append(newNode) #obtiene la referencia del nodo

  def shortest_path(self, s0, sf):
    pass

