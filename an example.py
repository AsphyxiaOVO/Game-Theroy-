import networkx as nx
import random

def create_complex_network():
    # 创建一个十个节点的网络图
    G = nx.Graph()
    edges = [
        ('A', 'B', 1), ('A', 'C', 2), ('B', 'D', 3), ('C', 'D', 2),
        ('B', 'E', 4), ('C', 'F', 5), ('D', 'G', 3), ('E', 'H', 2),
        ('F', 'I', 1), ('G', 'J', 2), ('H', 'J', 3), ('I', 'J', 2),
        ('source', 'A', 2), ('source', 'B', 3), ('source', 'C', 1)
    ]
    G.add_weighted_edges_from(edges)
    return G

class PotentialFunctionCalculator:
    def __init__(self, G, destination_nodes):
        self.G = G
        self.destination_nodes = destination_nodes

    def calculate_edge_cost(self, path, edge):
        """
        计算每条边的路径成本
        """
        if edge in zip(path, path[1:]):
            return 1
        return 0

    def calculate_potential_function(self, path_selection_profile):
        """
        计算潜在函数值
        """
        potential_function_value = 0  # 初始化潜在函数值为0
        for edge in self.G.edges:  # 对于图中的每条边e∈E，创建一个集合Q用于存储边e的目的地节点（Se），初始化边e的贡献度F(Se)为0，创建一个空集合B
            # 创建一个空列表Se
            Se = []
            for node in self.destination_nodes:
                cost = self.calculate_edge_cost(path_selection_profile[node], edge)
                if cost:
                    Se.append(node)
            F_Se = 0
            B = set()

            while Se:
                # 从Q中提取一个节点l，使得对于Q中的所有节点j，节点l的路径成本cl(p)大于或等于cj(p)
                # 定义一个函数，用于计算每个节点的所有边的代价之和
                def cost_funcone(node):
                    # 初始化总代价为0
                    total_cost = 0
                    # 遍历所有边
                    for e in self.G.edges:
                        # 调用self.calculate_edge_cost方法，计算边的代价
                        cost = self.calculate_edge_cost(path_selection_profile[node], e)
                        # 累加到总代价中
                        total_cost += cost
                    # 返回总代价
                    return total_cost

                # 定义一个函数，用于从一个列表中找出一个最大的元素
                def max_funcone(mylist):
                    # 初始化最大元素为列表的第一个元素
                    max_node = mylist[0]
                    # 初始化最大值为最大元素的代价
                    max_value = cost_funcone(max_node)
                    # 遍历列表中的其他元素
                    for node in mylist[1:]:
                        # 计算元素的代价
                        value = cost_funcone(node)
                        # 如果代价大于最大值
                        if value > max_value:
                            # 更新最大元素和最大值
                            max_node = node
                            max_value = value
                    # 返回最大元素
                    return max_node

                # 调用max_func函数，找出Se中的最大元素，赋值给l
                l = max_funcone(Se)
                # 将l添加到集合B中
                B.add(l)
                # 从Se中移除l
                Se.remove(l)

                # 从B中选择一个节点i，使得对于B中的所有节点k，节点i的路径成本ci(p)大于或等于ck(p)。
                # 定义一个函数，用于计算每个节点的所有边的代价之和
                def cost_functwo(node):
                    # 初始化总代价为0
                    total_cost = 0
                    # 遍历所有边
                    for e in self.G.edges:
                        # 调用self.calculate_edge_cost方法，计算边的代价
                        cost = self.calculate_edge_cost(path_selection_profile[node], e)
                        # 累加到总代价中
                        total_cost += cost
                    # 返回总代价
                    return total_cost

                # 定义一个函数，用于从一个集合中找出一个最大的元素
                def max_functwo(myset):
                    # 初始化最大元素为集合的第一个元素
                    max_node = next(iter(myset))
                    # 初始化最大值为最大元素的代价
                    max_value = cost_functwo(max_node)
                    # 遍历集合中的其他元素
                    for node in myset:
                        # 计算元素的代价
                        value = cost_functwo(node)
                        # 如果代价大于最大值
                        if value > max_value:
                            # 更新最大元素和最大值
                            max_node = node
                            max_value = value
                    # 返回最大元素
                    return max_node

                # 调用max_func函数，找出B中的最大元素，赋值给i
                i = max_functwo(B)
                # 将i的所有边的代价之和加到F_Se中
                F_Se += cost_functwo(i)  # 更新F(Se)的值为 F(Se) + ci(p)
            potential_function_value += F_Se  # 对每条边累加潜在函数值
        return potential_function_value

def calculate_path_cost(G, path):
    return sum(G[u][v]['weight'] for u, v in zip(path, path[1:]))


def find_pne(G, destination_nodes):
    """

    :G:网络图
    :destination_nodes: 目标节点
    :return: 找到的纳什均衡
    """
    path_selection_profile = {node: random.choice(list(nx.all_simple_paths(G, source='source', target=node)))
                              for node in destination_nodes}

    iteration = 0#初始化迭代次数为0
    while iteration < 3:  # 设置一个最小的迭代次数
        updated = False
        print(f"Iteration {iteration}:")
        for node in destination_nodes:
            current_path = path_selection_profile[node]
            calculator = PotentialFunctionCalculator(G, destination_nodes)
            print(f"  Current path for {node}: {current_path}, Cost: {calculate_path_cost(G, current_path)}, Potential Funcion Vlue:{calculator.calculate_potential_function(path_selection_profile)}")
            paths = list(nx.all_simple_paths(G, source='source', target=node))
            min_cost = calculate_path_cost(G, current_path)
            min_path = current_path

            for path in paths:
                cost = calculate_path_cost(G, path)
                if cost < min_cost:
                    min_cost = cost
                    min_path = path

            if min_path != current_path:
                path_selection_profile[node] = min_path
                updated = True

        iteration += 1

    return path_selection_profile

# 示例
G = create_complex_network()
destination_nodes = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
final_path_selection_profile = find_pne(G, destination_nodes)
calculator = PotentialFunctionCalculator(G, destination_nodes)

# 打印最终的结果
print("\nFinal Path Selection Profile:")
for node, path in final_path_selection_profile.items():
    print(f"  {node}: {path}, Cost: {calculate_path_cost(G, path)}, Potential Funcion Vlue:{calculator.calculate_potential_function(final_path_selection_profile)}")


