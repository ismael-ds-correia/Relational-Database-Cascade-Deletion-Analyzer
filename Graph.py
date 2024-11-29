from Vertex import Vertex


class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, vertex):
        if not any(v.name == vertex.name for v in self.vertices):
            self.vertices.append(vertex)

    def add_edge(self, from_vertex, to_vertex):
        from_vertex.add_adjacency(to_vertex)

    def get_vertex(self, name):
        for vertex in self.vertices:
            if vertex.name == name:
                return vertex
        return None

    def __str__(self):
        result = []
        for vertex in self.vertices:
            adjacencies = [v.name for v in vertex.adjacency_list]
            result.append(f"{vertex.name}: {', '.join(adjacencies)}")
        return "\n".join(result)

    def build_graph(self, filename):
        graph = Graph()

        with open(filename, 'r') as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                vertex_name = lines[i].strip()
                i += 1
                n_edges = int(lines[i].strip())
                i += 1

                vertex = graph.get_vertex(vertex_name)
                if vertex is None:
                    vertex = Vertex(vertex_name)
                    graph.add_vertex(vertex)

                for _ in range(n_edges):
                    adjacent_vertex_name = lines[i].strip()
                    adjacent_vertex = graph.get_vertex(adjacent_vertex_name)
                    if adjacent_vertex is None:
                        adjacent_vertex = Vertex(adjacent_vertex_name)
                        graph.add_vertex(adjacent_vertex)

                    graph.add_edge(vertex, adjacent_vertex)
                    i+=1

        return graph
























