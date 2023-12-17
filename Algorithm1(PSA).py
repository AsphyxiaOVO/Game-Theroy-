import networkx as nx
import random

def initialize_path_selection_profile(G, destination_nodes):
    """
    初始化每个目标节点为任意配置文件.
    """
    path_selection_profile = {}
    for node in destination_nodes:
        paths = list(nx.all_simple_paths(G, source='source', target=node))
        selected_path = random.choice(paths)
        path_selection_profile[node] = selected_path
    return path_selection_profile

def calculate_path_cost(path, G):
    """
    计算路径成本的方法（每个边的权重之和）
    """
    cost = 0
    for i in range(len(path) - 1):
        edge = (path[i], path[i + 1])
        cost += G.edges[edge]['weight']
    return cost

def update_path_selection_profile(G, path_selection_profile):
    """
    为每个节点更新路径选择
    """
    updated = False
    for node, current_path in path_selection_profile.items():
        paths = list(nx.all_simple_paths(G, source='source', target=node))
        min_cost = calculate_path_cost(current_path, G)
        min_path = current_path

        #历遍路径，检查是否有更低成本的路径
        for path in paths:
            cost = calculate_path_cost(path, G)
            if cost < min_cost:
                min_cost = cost
                min_path = path

        #如果有更低成本的路径就更新路径
        if min_path != current_path:
            path_selection_profile[node] = min_path
            updated = True

    return updated

#创建一个简单的网络图
G = nx.Graph()
G.add_edge('source', 'A', weight=1)
G.add_edge('A', 'B', weight=2)
G.add_edge('B', 'C', weight=3)
G.add_edge('source', 'D', weight=2)
G.add_edge('D', 'C', weight=1)
G.add_edge('A', 'D', weight=1)
destination_nodes = ['B', 'C']

#初始化路径选择策略
path_selection_profile = initialize_path_selection_profile(G, destination_nodes)

# 不断更新每个节点的路径选择，直到没有改变
while update_path_selection_profile(G, path_selection_profile):
    pass

print(path_selection_profile)
