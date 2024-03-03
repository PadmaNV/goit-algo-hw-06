import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import function

"""ЗАВДАННЯ 1 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

# Створення графа метро
metro_graph = nx.Graph()

# Додавання вершин (станцій)
stations = ["A", "B", "C", "D", "E", "F", "G"]
metro_graph.add_nodes_from(stations)

# Додавання ребер (зв'язків між станціями)
connections = [("A", "B"), ("B", "C"), ("D", "E"), ("E", "A"),
                ("E", "F"), ("A", "F"), ("B", "F"), ("G", "D"),
                ("F", "G"), ("G", "C")]
metro_graph.add_edges_from(connections)

# Візуалізація графа
nx.draw(metro_graph, with_labels=True, node_color='lightblue', font_weight='bold', node_size=1500)
plt.title("Граф метро")
plt.show()

# Аналіз основних характеристик графа
num_nodes = metro_graph.number_of_nodes()
num_edges = metro_graph.number_of_edges()
degree_sequence = sorted([d for n, d in metro_graph.degree()], reverse=True)


print("\nКількість вершин:", num_nodes)
print("Кількість ребер:", num_edges)
print("Ступінь вершин:", degree_sequence, "\n\n")


"""ЗАВДАННЯ 2 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
print(f"Знаходження шляхів руху в метро алгоритмом DFS: ")
function.dfs_recursive(metro_graph, 'A')

print("\nЗнаходження шляхів руху в метро алгоритмом BFS:")
function.bfs_recursive(metro_graph, deque(["A"]))


"""ЗАВДАННЯ 3 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

metro_graph.add_edge("A", "B", weight=2)
metro_graph.add_edge("B", "C", weight=4)
metro_graph.add_edge("D", "E", weight=6)
metro_graph.add_edge("E", "A", weight=3)
metro_graph.add_edge("E", "F", weight=6)
metro_graph.add_edge("A", "F", weight=3)
metro_graph.add_edge("B", "F", weight=3)
metro_graph.add_edge("G", "D", weight=2)
metro_graph.add_edge("F", "G", weight=4)
metro_graph.add_edge("G", "C", weight=6)

distances = function.dijkstra(metro_graph, 'A')

print("\n\nНайближча відстань від станії А до інших станцій:")
for node, distance in distances.items():
    print(f'{node} - {distance}')
