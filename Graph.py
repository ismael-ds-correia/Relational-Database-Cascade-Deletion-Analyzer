# A classe Vertex representa um vértice (ou nó) no grafo, que pode ter um nome e uma lista de adjacências.
class Vertex:
    def __init__(self, name=None):
        self.name = name  # Nome do vértice.
        self.adjacency_list = []  # Lista de adjacências (vértices para os quais este vértice tem uma aresta).

    # Método para adicionar um vértice à lista de adjacências (vértices para os quais este vértice aponta).
    def add_adjacency(self, vertex):
        self.adjacency_list.append(vertex)

    # Representação do vértice em formato string.
    def __str__(self):
        return f"Vertex({self.name})"


# A classe Graph representa o grafo como um todo, com vértices e suas conexões (arestas).
class Graph:
    def __init__(self):
        self.vertices = []  # Lista que armazena todos os vértices do grafo.

    # Adiciona um vértice ao grafo se ele ainda não existir.
    def add_vertex(self, vertex):
        if not any(v.name == vertex.name for v in self.vertices):
            self.vertices.append(vertex)

    # Cria uma aresta entre dois vértices, ou seja, o vértice 'from_vertex' aponta para o vértice 'to_vertex'.
    def add_edge(self, from_vertex, to_vertex):
        from_vertex.add_adjacency(to_vertex)

    # Retorna um vértice do grafo com o nome especificado. Retorna None se o vértice não existir.
    def get_vertex(self, name):
        for vertex in self.vertices:
            if vertex.name == name:
                return vertex
        return None

    # Representação em string do grafo, mostrando cada vértice e suas adjacências.
    def __str__(self):
        result = []
        for vertex in self.vertices:
            adjacencies = [v.name for v in vertex.adjacency_list]  # Obtem os nomes dos vértices adjacentes.
            result.append(f"{vertex.name}: {', '.join(adjacencies)}")  # Formata a string de representação.
        return "\n".join(result)

    # Constrói o grafo a partir de um arquivo de entrada, onde a estrutura do arquivo é descrita abaixo.
    def build_graph(self, filename):
        graph = Graph()  # Cria um novo grafo vazio.

        # Abre o arquivo para leitura.
        with open(filename, 'r') as file:
            lines = file.readlines()  # Lê todas as linhas do arquivo.
            i = 0  # Índice para percorrer as linhas do arquivo.

            # Itera sobre as linhas do arquivo para construir o grafo.
            while i < len(lines):
                vertex_name = lines[i].strip()  # Nome do vértice.
                i += 1  # Avança para a próxima linha.
                n_edges = int(lines[i].strip())  # Número de vértices aos quais este vértice está ligado (arestas).
                i += 1  # Avança para a próxima linha.

                # Busca o vértice no grafo ou cria um novo se não encontrar.
                vertex = graph.get_vertex(vertex_name)
                if vertex is None:
                    vertex = Vertex(vertex_name)  # Cria o novo vértice.
                    graph.add_vertex(vertex)  # Adiciona ao grafo.

                # Adiciona as arestas para os vértices adjacentes.
                for _ in range(n_edges):
                    adjacent_vertex_name = lines[i].strip()  # Nome do vértice adjacente.
                    adjacent_vertex = graph.get_vertex(adjacent_vertex_name)

                    if adjacent_vertex is None:
                        adjacent_vertex = Vertex(adjacent_vertex_name)  # Cria o vértice adjacente.
                        graph.add_vertex(adjacent_vertex)  # Adiciona ao grafo.

                    graph.add_edge(vertex, adjacent_vertex)  # Adiciona a aresta do vértice atual para o adjacente.
                    i += 1  # Avança para a próxima linha.

        return graph  # Retorna o grafo construído.

    # Calcula o efeito de exclusão em cascata a partir de um vértice específico.
    def cascade_effect(self, vertex):
        excluded = set()  # Conjunto para armazenar os vértices excluídos (sem duplicação).
        stack = [vertex]  # Pilha para realizar a busca em profundidade (DFS).

        # Realiza a busca em profundidade para encontrar todos os vértices excluídos em cascata.
        while stack:
            v = stack.pop()  # Pega o próximo vértice da pilha.
            if v.name not in excluded:  # Verifica se o vértice já foi excluído.
                excluded.add(v.name)  # Marca o vértice como excluído.
                for adj in v.adjacency_list:  # Para cada vértice adjacente, adicione à pilha.
                    stack.append(adj)

        return excluded  # Retorna o conjunto de vértices excluídos.

    # Mostra os efeitos da exclusão de cada vértice, ou seja, os vértices que seriam excluídos em cascata.
    def show_cascade_effects(self):
        effects = {}  # Dicionário para armazenar os efeitos de exclusão para cada vértice.
        for vertex in self.vertices:
            excluded = self.cascade_effect(vertex)  # Calcula o efeito de exclusão em cascata.
            effects[vertex.name] = excluded  # Armazena no dicionário.

        # Exibe os resultados para cada vértice.
        for vertex_name, excluded in effects.items():
            print(f"Se o vértice {vertex_name} for excluído, os seguintes vértices serão deletados em cascata:")
            print(", ".join(excluded))  # Mostra os vértices excluídos.
            print("-" * 40)  # Linha separadora para melhor leitura.
