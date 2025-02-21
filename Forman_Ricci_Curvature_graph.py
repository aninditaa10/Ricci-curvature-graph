
import networkx as nx
from GraphRicciCurvature.FormanRicci import FormanRicci 
import matplotlib.pyplot as plt
import logging

# Created a directed graph
G = nx.DiGraph()

# Added nodes (ignoring colors, all nodes are treated same)
nodes = ["S3A", "S3B", "S3G", "S3H", "S2C", "S2D", "S2I", "S1E", "S1L", "TC", "R1K", "R1M", "R2N", "R2O", "R3R", "R3S", "R3T"]
G.add_nodes_from(nodes)

edges = [
    ("S3A", "S2C", 1),
    ("S3B", "S2D", 3),
    ("S3G", "S2I", 1),
    ("S3H", "S2I", 2),
    ("S2C", "S1E", 2),
    ("S2C", "R1K", 1),
    ("S2D", "S1E", 2),
    ("S2I", "R1K" ,6),
    ("S2I", "S1L", 4),
    ("S2I", "R1M", 5),
    ("S1E", "TC", 3),
    ("S1L", "TC", 6),
    ("TC", "R1K", 4),
    ("TC", "R1M", 3),
    ("R1K", "R2N", 4),
    ("R1M", "R2O", 2),
    ("R2N", "R3R", 1),
    ("R2N", "R3S", 5),
    ("R2O", "R3T", 4),
    ("R3S", "R3T", 2)
 ]

for u, v, w in edges:
 G.add_edge(u, v, weight=w)

# Had to convert Node Labels to Integers (to satisfy the library's logging formatter)
mapping = {node: i for i, node in enumerate(G.nodes())}
inv_mapping = {i: node for node, i in mapping.items()}
H = nx.relabel_nodes(G, mapping)

# Computed Forman Ricci Curvature on the Graph
frc = FormanRicci(H,weight='weight')
frc.compute_ricci_curvature()
print(H.edges(data=True))

print("Edges with computed Forman Ricci curvature:")
for u, v, data in H.edges(data=True):
    print(f"Edge ({u} -> {v}): {data}")

# Stored curvature values in edge attributes
for (u, v) in H.edges():
    H[u][v]['formanCurvature'] = frc.G[u][v].get('formanCurvature', None)  # Ensure assignment

# Extracted curvature values for each edge
curvature_values = nx.get_edge_attributes(H, 'formanCurvature')

print("Forman Ricci Curvature for each edge:")
for edge, curvature in curvature_values.items():
    print(f"Edge {edge}: {curvature}")

edge_labels = {}
for (u, v, data) in H.edges(data=True):
    w = data.get('weight', 0)
    c = data.get('formanCurvature', 0)
    edge_labels[(u, v)] = f"w={w}, c={c:.2f}"

# Defined the correct node labels again
node_names = ["S3A", "S3B", "S3G", "S3H", "S2C", "S2D", "S2I", "S1E", "S1L", "TC",
              "R1K", "R1M", "R2N", "R2O", "R3R", "R3S", "R3T"]
label_mapping = {i: name for i, name in enumerate(node_names)}

H = nx.relabel_nodes(H, label_mapping)

# Preparing the figure using a layout that spaces nodes more evenly
plt.figure(figsize=(12, 8))

pos = nx.kamada_kawai_layout(H)

nx.draw_networkx_nodes(H, pos, node_color="lightblue", node_size=500, edgecolors='black')
nx.draw_networkx_edges(H, pos, edge_color="gray", arrows=True, arrowstyle='-|>', arrowsize=20, width=2)

nx.draw_networkx_labels(H, pos, font_size=6, font_weight='bold')

# Preparing edge labels showing the curvature
edge_labels = {(u, v): round(H[u][v]["formanCurvature"], 3) for (u, v) in H.edges()}
nx.draw_networkx_edge_labels(H, pos, edge_labels=edge_labels, font_color="red", font_size=8)

plt.title("Directed Graph with Forman-Ricci Curvature on Edges", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()