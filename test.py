from Graph import Graph

filename = "file/path"

graph = Graph()

graph = graph.build_graph(filename)

print(graph)

graph.show_cascade_effects()