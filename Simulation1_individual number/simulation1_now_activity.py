import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import csv
random.seed(43)
np.random.seed(43)
n=1000
# 创建Watts-Strogatz图
kinds = ["S", "I", "R"]

graph = nx.generators.random_graphs.watts_strogatz_graph(n, 4, 0.7, 42)  ########## 平均度数影响活动潜力 4为平均度数
node_degrees = dict(graph.degree())
total_degree_sum = sum(node_degrees.values())
eta=110  #################### 改
node_active = {node: degree / total_degree_sum*eta for node, degree in node_degrees.items()} ###此处没有进行计算activity 要调整activity在后面
node_infect_rate= {}
node_kind={}
infect_rate_i={};recover_rate_i={}
day={}
r_recover_rate={}
infection_probability={}
infection_probability1={}
for i in range(n):
    node_kind[i] = kinds[0]
    infection_probability[i]=0
    recover_rate_i[i]=0.00
    infection_probability1[i]=0
    day[i]=0
    node_infect_rate[i] = 1*np.random.lognormal(-2, 0.5) #### 重要
#node_infect_rate = {}

# 指定CSV文件名
# csv_file_name = 'my_dict.csv'
#
# # 打开CSV文件以读取数据
# with open(csv_file_name, mode='r') as file:
#     reader = csv.DictReader(file)
#     # 遍历CSV文件中的每一行数据
#     for row in reader:
#         node = eval(row['Node'])
#         infect_rate = float(row['Infection Rate'])
#         # 将数据分配给字典的键和值
#         node_infect_rate[node] = infect_rate

# 随机选择一个节点变为I状态
#initial_infected_node = random.choice(list(graph.nodes()))
initial_infected_node = 41
print(initial_infected_node)
node_kind[initial_infected_node] = kinds[1]
num_steps = 1500               ################################# 待改
s_counts=[]
infected_counts = []
recovered_counts = []
s_infection_counts=[]
r_infection_counts=[]
for step in range(num_steps):
    print(step)
    new_infections = {}
    new_recoveries = {}
    if step<5000:
        num_new_nodes = min(4, max(0, int(np.random.poisson(0.17))))
        for _ in range(num_new_nodes):
            new_node = max(graph.nodes()) + 1  # 生成一个新的节点
            graph.add_node(new_node)
            neighbors_to_connect = random.sample(list(graph.nodes()), random.randint(2, 6))
            graph.add_edges_from([(new_node, neighbor) for neighbor in neighbors_to_connect])
            node_kind[new_node] = random.choices(kinds, weights=[0.2, 0.1, 0.15], k=1)[0]
            node_infect_rate[new_node]=1*np.random.lognormal(-2, 0.5)   ############################################ 待改
            day[new_node]=0
            infection_probability[new_node]=0
            recover_rate_i[new_node]=0
            infection_probability1[new_node]=0
            # 随机迁出节点
        if step<=1000:
            num_nodes_to_remove = num_new_nodes
            for _ in range(num_nodes_to_remove):
                nodes_to_remove = []
                select_kind = random.choices(kinds, weights=[0.2, 0.1, 0.15], k=1)[0]
                kind_nodes = [node for node in graph.nodes() if node_kind[node] == select_kind]
                num_nodes_to_remove_by_kind = min(1, len(kind_nodes))
                a=random.sample(kind_nodes, num_nodes_to_remove_by_kind)
                graph.remove_nodes_from(a)
        if step>1000:
            # 随机迁出节点
            num_nodes_to_remove = num_new_nodes
            for _ in range(num_nodes_to_remove):
                nodes_to_remove=[]
                select_kind=random.choices(kinds, weights=[0.2, 0.1, 0.15], k=1)[0]
                kind_nodes = [node for node in graph.nodes() if node_kind[node] == select_kind]
                num_nodes_to_remove_by_kind = min(1, len(kind_nodes))
                nodes_to_remove.extend(random.sample(kind_nodes, num_nodes_to_remove_by_kind))
                graph.remove_nodes_from(nodes_to_remove)
    node_degrees = dict(graph.degree())
    total_degree_sum = sum(node_degrees.values())
    for node in graph.nodes():
        node_active[node] = node_degrees[node] / total_degree_sum * eta
    for node in graph.nodes():
        infection_probability1[node]=0
        infect_neighbor=[]
        if node_kind[node] == kinds[1]:  # 如果节点是感染者
            # 计算该节点对相邻节点的感染
            for neighbor in graph.neighbors(node):
                infect_neighbor.append(node_active[node] * node_active[neighbor] * node_infect_rate[node])
                if node_kind[neighbor] == kinds[0]:  # 仅感染未感染的节点
                    infection_probability[node] =node_active[node] * node_active[neighbor] * node_infect_rate[node]*3.1
                    if random.random() < infection_probability[node]:
                    #new_infections[neighbor] = new_infections.get(neighbor, 0) + 1
                        new_infections[neighbor]=1
                        infection_probability1[neighbor]=infection_probability[node]
            # 更新节点的康复和迁移情况
            if node_kind[node] == kinds[1]:  # 仅对感染者进行更新
                if day[node] <= 30:
                    day[node] = day[node] + 1
                if day[node] >=7:
                    recover_rate_i[node] = (math.exp(day[node] / 4000) - 1)  ############infection rate待改
                # 计算节点的康复
                if random.random() < recover_rate_i[node]:
                    new_recoveries[node] = 1

    # 更新感染者和康复者的状态
    s_infection = 0
    r_infection = 0
    for node, infections in new_infections.items():
        node_kind[node] = kinds[1]
        infect_rate_i[node] = infections
        s_infection = s_infection + infection_probability1[node]
    for node, recoveries in new_recoveries.items():
        r_infection = r_infection +recover_rate_i[node]
        node_kind[node] = kinds[2]
    s_count=0
    i_count=0
    r_count=0
    for node in graph.nodes():
        if node_kind[node]=='S':
            s_count=s_count+1
        if node_kind[node]=='I':
            i_count=i_count+1
        if node_kind[node]=='R':
            r_count=r_count+1
    s_counts.append(s_count)
    infected_counts.append(i_count)
    recovered_counts.append(r_count)
    s_infection_counts.append(s_infection)
    r_infection_counts.append(r_infection)
plt.figure(figsize = (10,6))
plt.plot(range(num_steps), s_counts, label='S')
plt.plot(range(num_steps), infected_counts, label='I')
plt.plot(range(num_steps), recovered_counts, label='R')
with open('result_activity1.1.csv', 'w', newline= '') as f:   ################################################# 待改
     writer = csv.writer(f)
     writer.writerow(s_counts)
     writer.writerow(infected_counts)
     writer.writerow(recovered_counts)
plt.legend()
# averages_s = [sum(s_infection_counts[i:i+10]) / 10 for i in range(0, len(s_infection_counts) - 9)]
# averages = [sum(r_infection_counts[i:i+10]) /10 for i in range(0, len(r_infection_counts) - 9)]
# x_data = np.arange(len(averages))
# averages=averages[0::25]
# averages_s=averages_s[0::25]
# x_data=x_data[0::25]
# plt.figure(2)
# def normal_distribution(x, mu, std, A):
#     return A * np.exp(-((x - mu) ** 2) / (2 * std ** 2))
# initial_guess = [x_data[np.argmax(averages)], 10, 2.0]
# from scipy.optimize import curve_fit
# params, covariance = curve_fit(normal_distribution, x_data, averages, p0=initial_guess)
# # 得到拟合的参数
# mu,std,A= params
# # 使用拟合的参数生成拟合曲线
# fit_curve = normal_distribution(x_data, mu, std, A)
# fit_curve0 = fit_curve
# # 绘制原始数据和拟合曲线
# plt.plot(x_data, averages)
# plt.plot(x_data, fit_curve0, color='red')
# plt.figure(3)
# def normal_distribution(x, mu, std, A):
#     return A * np.exp(-((x - mu) ** 2) / (2 * std ** 2))
# initial_guess = [x_data[np.argmax(averages_s)], 10, 2.0]  # 初始猜测的参数值
# params, covariance = curve_fit(normal_distribution, x_data, averages_s, p0=initial_guess)
# mu, std, A = params
#
# # 使用拟合的参数生成拟合曲线
# fit_curve = normal_distribution(x_data, mu, std, A)
# fit_curve1 = fit_curve
# # 绘制原始数据和拟合曲线
# plt.plot(x_data, averages_s)
# plt.plot(x_data, fit_curve1, color='red')
# plt.figure(4)
# result=[]
# x=[]
# for i in range(len(fit_curve0)):
#     if fit_curve0[i] !=0:
#         result.append(fit_curve1[i]/fit_curve0[i])
#         x.append(x_data[i])
# plt.plot(x,result)
# with open('qianru_no.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['x', 'result'])  # 写入CSV文件的表头
#     # 将 x 和 result 写入数据行
#     for i in range(len(x)):
#         writer.writerow([x[i], result[i]])
plt.show()
