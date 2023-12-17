import networkx as nx
import matplotlib.pyplot as plt

def create_network():
    # 创建一个有十个节点的网络
    G = nx.Graph()
    edges = [
        ('A', 'B', 1), ('A', 'C', 2), ('B', 'D', 3), ('C', 'D', 2),
        ('B', 'E', 4), ('C', 'F', 5), ('D', 'G', 3), ('E', 'H', 2),
        ('F', 'I', 1), ('G', 'J', 2), ('H', 'J', 3), ('I', 'J', 2),
        ('source', 'A', 2), ('source', 'B', 3), ('source', 'C', 1)
    ]
    G.add_weighted_edges_from(edges)
    return G

# 创建网络
G = create_network()

# 画出网络图
pos = nx.spring_layout(G)  # 节点的位置
labels = nx.get_edge_attributes(G, 'weight')
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='black', linewidths=1, font_size=15)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Network Graph")
plt.show()
