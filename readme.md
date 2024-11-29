# Relational Database Cascade Deletion Analyzer

Este projeto simula a exclusão em cascata de entidades em um banco de dados, utilizando grafos para representar as relações de dependência entre elas. Ele permite construir um grafo a partir de um arquivo de entrada e analisar quais entidades seriam impactadas caso uma delas fosse excluída.

---

## Funcionalidades

- **Construção de Grafos**: Construa um grafo direcionado a partir de um arquivo de entrada, onde cada nó representa uma entidade e cada aresta representa uma dependência entre entidades.
- **Exclusão em Cascata**: Determine quais entidades seriam excluídas em cascata ao remover um nó específico.
- **Visualização de Impactos**: Exibe, para cada nó, os impactos potenciais de sua remoção no grafo.
- **Classes Modulares**: Estrutura clara e organizada com classes `Vertex` (para nós) e `Graph` (para grafos).

---

## Como Funciona

### Classes

- **Vertex**: Representa um vértice (entidade) no grafo. Contém o nome do vértice e uma lista de adjacências (dependências).
  
  Métodos:
  - `add_adjacency(vertex)`: Adiciona uma aresta do vértice atual para outro vértice.
  - `__str__()`: Representação em string do vértice.

- **Graph**: Representa o grafo como um todo. Contém a lista de vértices e oferece métodos para manipulação do grafo.

  Métodos:
  - `add_vertex(vertex)`: Adiciona um vértice ao grafo, caso não exista.
  - `add_edge(from_vertex, to_vertex)`: Cria uma aresta entre dois vértices.
  - `get_vertex(name)`: Retorna o vértice pelo nome.
  - `build_graph(filename)`: Constrói o grafo a partir de um arquivo de entrada.
  - `cascade_effect(vertex)`: Calcula os vértices que seriam excluídos em cascata caso o vértice fornecido seja removido.
  - `show_cascade_effects()`: Exibe os efeitos da exclusão em cascata de cada vértice.

### Arquivo de Entrada

O arquivo de entrada deve conter as informações sobre os vértices e suas dependências. Cada vértice é seguido pelo número de arestas que ele possui e, em seguida, os vértices referenciados. Um exemplo de arquivo:

```txt
A
3
B
C
D
B
2
E
F
C
1
G
D
0
E
1
A
F
1
G
G
0
