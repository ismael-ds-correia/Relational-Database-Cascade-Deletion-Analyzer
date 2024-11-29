# A classe Vertex representa um vértice (ou nó) em um grafo. Cada vértice pode ter um nome
# e uma lista de adjacências (vértices para os quais este vértice tem uma aresta).
class Vertex:
    # O construtor da classe Vertex inicializa o nome do vértice e a lista de adjacências.
    # O parâmetro 'name' define o nome do vértice, e a lista de adjacências é inicializada vazia.
    def __init__(self, name=None):
        self.name = name  # O nome do vértice, fornecido ao criar o vértice.
        self.adjacency_list = []  # A lista de adjacências. Inicialmente, é uma lista vazia.

    # Método para adicionar um vértice à lista de adjacências (ou seja, o vértice atual "aponta" para o vértice passado como argumento).
    def add_adjacency(self, vertex):
        self.adjacency_list.append(vertex)  # Adiciona o vértice 'vertex' à lista de adjacências do vértice atual.

    # Método especial que define a representação do vértice quando este é convertido para string.
    def __str__(self):
        return f"Vertex({self.name})"  # Retorna uma string representando o vértice pelo seu nome.
