import networkx as nx
import matplotlib.pyplot as plt


def get_adjacency_matrix():

    n = int(input("Введите количество вершин: "))


    adj_matrix = []
    print("Введите матрицу смежности построчно (через пробелы):")


    for i in range(n):
        row = list(map(int, input(f"Строка {i + 1}: ").split()))
        if len(row) != n:
            print("Ошибка: количество элементов в строке не совпадает с размером матрицы.")
            return None
        adj_matrix.append(row)

    return adj_matrix


def draw_graph_from_adjacency_matrix(adj_matrix):
    if adj_matrix is None:
        print("Невозможно построить граф из-за ошибки в вводе данных.")
        return

    G = nx.Graph()


    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] != 0:  
                G.add_edge(i, j, weight=adj_matrix[i][j])


    pos = nx.spring_layout(G)


    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=700, font_size=15)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()



adj_matrix = get_adjacency_matrix()
draw_graph_from_adjacency_matrix(adj_matrix)
