import networkx as nx

class PotentialFunctionCalculator:
    def __init__(self, G, destination_nodes):
        """
        初始化潜在函数值
        : G:网络图
        : destination_nodes:目的节点列表
        """
        self.G = G
        self.destination_nodes = destination_nodes

    def calculate_edge_cost(self, path, edge):
        """
        计算路径成本
        :path: 路径列表
        :edge:边的元组
        :return:路径成本
        """
        if edge in zip(path, path[1:]):
            return 1
        return 0

    def calculate_potential_function(self, path_selection_profile):
        """
        计算潜在函数值
        """
        potential_function_value = 0#初始化潜在函数值为0
        for edge in self.G.edges:#对于图中的每条边e∈E，创建一个集合Q用于存储边e的目的地节点（Se），初始化边e的贡献度F(Se)为0，创建一个空集合B
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

                #从B中选择一个节点i，使得对于B中的所有节点k，节点i的路径成本ci(p)大于或等于ck(p)。
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
                F_Se += cost_functwo(i) #更新F(Se)的值为 F(Se) + ci(p)
            potential_function_value += F_Se#对每条边累加潜在函数值
        return potential_function_value

# 示例
G = nx.Graph()
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C')])
destination_nodes = ['A', 'B', 'C', 'D']
path_selection_profile = {'A': ['A', 'B', 'C'], 'B': ['B', 'C', 'D'], 'C': ['C', 'D', 'A'], 'D': ['D', 'A', 'B']}

calculator = PotentialFunctionCalculator(G, destination_nodes)
potential_function_value = calculator.calculate_potential_function(path_selection_profile)
print(potential_function_value)

