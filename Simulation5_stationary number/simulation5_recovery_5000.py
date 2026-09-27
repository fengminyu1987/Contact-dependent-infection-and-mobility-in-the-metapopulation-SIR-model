import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import csv
random.seed(41)
np.random.seed(41)
n=3000
# create Watts-Strogatz network
kinds = ["S", "I", "R"]
sigma_scale = -2.25
recovery_scale=5000
num_steps = 2000               #################################

csv_file_list=["5_mu_5000-3.00.csv", "5_mu_5000-2.98.csv", "5_mu_5000-2.96.csv", "5_mu_5000-2.94.csv", "5_mu_5000-2.92.csv",
                 "5_mu_5000-2.90.csv", "5_mu_5000-2.88.csv", "5_mu_5000-2.86.csv", "5_mu_5000-2.84.csv", "5_mu_5000-2.82.csv",
                 "5_mu_5000-2.80.csv", "5_mu_5000-2.78.csv", "5_mu_5000-2.76.csv", "5_mu_5000-2.74.csv", "5_mu_5000-2.72.csv",
                 "5_mu_5000-2.70.csv", "5_mu_5000-2.68.csv", "5_mu_5000-2.66.csv", "5_mu_5000-2.64.csv", "5_mu_5000-2.62.csv",
                 "5_mu_5000-2.60.csv", "5_mu_5000-2.58.csv", "5_mu_5000-2.56.csv", "5_mu_5000-2.54.csv", "5_mu_5000-2.52.csv",
                 "5_mu_5000-2.50.csv", "5_mu_5000-2.48.csv", "5_mu_5000-2.46.csv", "5_mu_5000-2.44.csv", "5_mu_5000-2.42.csv",
                 "5_mu_5000-2.40.csv", "5_mu_5000-2.38.csv", "5_mu_5000-2.36.csv", "5_mu_5000-2.34.csv", "5_mu_5000-2.32.csv",
                 "5_mu_5000-2.30.csv", "5_mu_5000-2.28.csv", "5_mu_5000-2.26.csv", "5_mu_5000-2.24.csv", "5_mu_5000-2.22.csv",
                 "5_mu_5000-2.20.csv", "5_mu_5000-2.18.csv", "5_mu_5000-2.16.csv", "5_mu_5000-2.14.csv", "5_mu_5000-2.12.csv",
                 "5_mu_5000-2.10.csv", "5_mu_5000-2.08.csv", "5_mu_5000-2.06.csv", "5_mu_5000-2.04.csv", "5_mu_5000-2.02.csv",
                 "5_mu_5000-2.00.csv"]
for file in csv_file_list:

   graph = nx.generators.random_graphs.watts_strogatz_graph(n, 12, 0.7, 42)  ########## 平均度数影响活动潜力 4为平均度数
   node_degrees = dict(graph.degree())
   total_degree_sum = sum(node_degrees.values())

   eta=300  #################### 改
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
       node_infect_rate[i] = 1*np.random.lognormal(sigma_scale, 0.5) #### 重要

# 随机选择一个节点变为I状态
#initial_infected_node = random.choice(list(graph.nodes()))
   initial_infected_node = 41
   print(initial_infected_node)
   node_kind[initial_infected_node] = kinds[1]

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
         num_new_nodes = min(4, max(0, int(np.random.poisson(0.3))))
         for _ in range(num_new_nodes):
            new_node = max(graph.nodes()) + 1  # 生成一个新的节点
            graph.add_node(new_node)
            neighbors_to_connect = random.sample(list(graph.nodes()), random.randint(10, 14))
            graph.add_edges_from([(new_node, neighbor) for neighbor in neighbors_to_connect])
            node_kind[new_node] = random.choices(kinds, weights=[0.2, 0.1, 0.15], k=1)[0]
            node_infect_rate[new_node]=1*np.random.lognormal(sigma_scale, 0.3)   ############################################ 待改
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
         ########################## 改活动率
         node_active[node] = node_degrees[node] / total_degree_sum * eta
      for node in graph.nodes():
         infection_probability1[node]=0
         infect_neighbor=[]
         if node_kind[node] == kinds[1]:  # 如果节点是感染者
            # 计算该节点对相邻节点的感染
            for neighbor in graph.neighbors(node):
               infect_neighbor.append(node_active[node] * node_active[neighbor] * node_infect_rate[node])
               if node_kind[neighbor] == kinds[0]:  # 仅感染未感染的节点
                  infection_probability[node] = node_active[node] * node_active[neighbor] * node_infect_rate[node]
                  if random.random() < infection_probability[node]:
                    #new_infections[neighbor] = new_infections.get(neighbor, 0) + 1
                     new_infections[neighbor]=1
                     infection_probability1[neighbor]=infection_probability[node]
            # 更新节点的康复和迁移情况
            if node_kind[node] == kinds[1]:  # 仅对感染者进行更新
               if day[node] <= 30:
                  day[node] = day[node] + 1
               if day[node] >=7:
                  recover_rate_i[node] = (math.exp(day[node] / recovery_scale) - 1)  ############infection rate待改
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
   #plt.plot(range(num_steps), infected_counts, label='I')
   #plt.plot(range(num_steps), recovered_counts, label='R')

   with open(file, 'w', newline= '') as f:   ################################################# 待改
      writer = csv.writer(f)
      writer.writerow(s_counts)
      #writer.writerow(infected_counts)
      #writer.writerow(recovered_counts)
   plt.legend()
   sigma_scale+=0.005
   print(sigma_scale)

plt.show()
