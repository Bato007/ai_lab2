
# Obtener el path del grafo y lo convierte
# a un array [[v11, v12, w], ..., [vm1, vm2, wm]]
def read_document(path):
  pass

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
    self.relations.push(Edge(self.node, f_none, w))

  def get_nodes(self):
    return self.relations

  def get_node(self):
    return self.node

# Clase grafo
class Graph(object):

  def __init__(self, array):
    pass

  def shortest_path(self, s0, sf):
    pass

