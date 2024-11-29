from Graph import Graph

filename = "C:/Users/Diogenes/PycharmProjects/RelationalDatabaseCascadeDeletionAnalyzer/input.txt"

graph = Graph()

graph = graph.build_graph(filename)

print(graph)

graph.show_cascade_effects()