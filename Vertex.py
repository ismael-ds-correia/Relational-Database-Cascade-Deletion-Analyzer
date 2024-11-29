class Vertex:
    def __init__(self, name=None):
        self.name = name
        self.id = None
        self.adjacency_list = []

    def add_adjacency(self, vertex):
        self.adjacency_list.append(vertex)

    def __str__(self):
        return f"Vertex({self.name})"