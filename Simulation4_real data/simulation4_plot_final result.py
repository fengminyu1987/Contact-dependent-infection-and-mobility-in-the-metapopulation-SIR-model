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



graph = nx.generators.random_graphs.watts_strogatz_graph(n, 100, 0.7, 42)  ########## 平均度数影响活动潜力 4为平均度数
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

sigma=-3.61
recovery_scale=1000

for i in range(n):
    node_kind[i] = kinds[0]
    infection_probability[i]=0
    recover_rate_i[i]=0.00
    infection_probability1[i]=0
    day[i]=0
    node_infect_rate[i] = 1*np.random.lognormal(sigma, 0.5) #### 重要
#node_infect_rate = {}
num_steps=32
initial_infected_node = 41
#print(initial_infected_node)
node_kind[initial_infected_node] = kinds[1]
initial_infected_node = 42
#print(initial_infected_node)
node_kind[initial_infected_node] = kinds[1]
initial_infected_node = 43
node_kind[initial_infected_node] = kinds[1]
initial_infected_node = 44
node_kind[initial_infected_node] = kinds[1]
initial_infected_node = 45
node_kind[initial_infected_node] = kinds[1]
initial_infected_node = 46
node_kind[initial_infected_node] = kinds[1]
initial_infected_node = 47
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
    if step<70:
        num_new_nodes = min(4, max(0, int(np.random.poisson(0.17))))
        for _ in range(num_new_nodes):
            new_node = max(graph.nodes()) + 1  # 生成一个新的节点
            graph.add_node(new_node)
            neighbors_to_connect = random.sample(list(graph.nodes()), random.randint(90,110))
            graph.add_edges_from([(new_node, neighbor) for neighbor in neighbors_to_connect])
            node_kind[new_node] = random.choices(kinds, weights=[0.3, 0.1, 0.15], k=1)[0]
            node_infect_rate[new_node]=1*np.random.lognormal(sigma, 0.5)   ############################################ 待改
            day[new_node]=0
            infection_probability[new_node]=0
            recover_rate_i[new_node]=0
            infection_probability1[new_node]=0
            # 随机迁出节点
        if step<=7:
            num_nodes_to_remove = num_new_nodes
            for _ in range(num_nodes_to_remove):
                nodes_to_remove = []
                select_kind = random.choices(kinds, weights=[19, 3, 0], k=1)[0]
                kind_nodes = [node for node in graph.nodes() if node_kind[node] == select_kind]
                num_nodes_to_remove_by_kind = min(1, len(kind_nodes))
                a=random.sample(kind_nodes, num_nodes_to_remove_by_kind)
                graph.remove_nodes_from(a)
        if step>7:
            # 随机迁出节点
            num_nodes_to_remove = num_new_nodes
            for _ in range(num_nodes_to_remove):
                nodes_to_remove=[]
                select_kind=random.choices(kinds, weights=[0.03, 0.12, 0.15], k=1)[0]
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
                    infection_probability[node] =node_active[node] * node_active[neighbor] * node_infect_rate[node]
                    if random.random() < infection_probability[node]:
                    #new_infections[neighbor] = new_infections.get(neighbor, 0) + 1
                        new_infections[neighbor]=1
                        infection_probability1[neighbor]=infection_probability[node]
            # 更新节点的康复和迁移情况
            if node_kind[node] == kinds[1]:  # 仅对感染者进行更新
                if day[node] <= 30:
                    day[node] = day[node] + 1
                if day[node] >=7:
                    recover_rate_i[node] = 1*(math.exp(day[node] / recovery_scale) - 1)  ############infection rate待改
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
import pandas as pd
import matplotlib.dates as mdates
from matplotlib.pyplot import MultipleLocator
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error

import warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['SimHei']   # 显示中文
plt.rcParams['axes.unicode_minus'] = False      # 显示负号

# date_list = pd.date_range(start='2022/3/1', end='2022/5/10')
# date_str_list = [str(i.year)+str(i.month).zfill(2)+str(i.day).zfill(2) for i in date_list]

path = '上海2022年3月疫情统计数据.xlsx'
df_city = pd.read_excel(path)

# 将日期列转换为日期类型
df_city['日期'] = pd.to_datetime(df_city['日期'], format='%Y年%m月%d日')

# 选择3月1日到5月10日的数据
start_date = pd.Timestamp('2022-03-01')
end_date = pd.Timestamp('2022-05-10')
df_city = df_city[(df_city['日期'] >= start_date) & (df_city['日期'] <= end_date)]

print(df_city)
# fig = plt.figure(figsize=(10, 6))
# ax = fig.add_subplot(111)
# plt.tick_params(labelsize=15)
#
# ax.plot_date(df_city['日期'], df_city['新增确诊病例'], 'o-', label='每日新增确诊病例')
# ax.plot_date(df_city['日期'], df_city['新增无症状感染者'], 'o-', label='每日新增易感染者')
#
# plt.ylabel('人数', fontsize=15)
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d\n%Y'))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=4))
#
# plt.legend(fontsize=12)  # 添加图例
# plt.tight_layout()  # 调整子图之间的间距
# plt.show()



############################## 画出结果的两个图
# 第一个子图，放置在位置(0, 0)
# ax1 = fig.add_subplot(211)
# ax1.plot_date(df_city['日期'], df_city['累计确诊']-df_city['累计治愈出院'], marker='+', label='Real data', color="red")
# # ax1.plot_date(df_city['日期'], infected_counts, 'o-',  color="#D85356", linewidth=3, label='I')
# # ax1.plot_date(df_city['日期'], df_city['新增无症状感染者'], 'o-', label='每日新增无症状感染者')
# ax1.set_ylabel('N', fontsize=15)
# ax1.xaxis.set_major_formatter(mdat
# # ax2.legend(fontsize=12, frameon=False)
# # ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d\n%Y'))  # 设置横坐标日期格式
# #
# # ax1 = fig.add_subplot(211)
# # #df_city["日期"] = df_city["日期"] + pd.Timedelta(days=30)
# #
# # ax1.plot_date(df_city['日期'], df_city['累计确诊']-df_city['累计治愈出院'], label='Real data', fmt="bo-", markeredgewidth=.006)
# # # ax1.plot_date(df_city['日期'], infected_counts, 'o-',  color="#D85356", linewidth=3, label='I')
# # # ax1.plot_date(df_city['日期'], df_city['新增无症状感染者'], 'o-es.DateFormatter('%m-%d\n%Y'))
# ax1.tick_params(labelsize=12)
# ax1.legend(fontsize=12)
#
# ax2 = fig.add_subplot(212)
# ax2.plot(df_city['日期'], infected_counts,  linewidth=3, label='I', marker="o", color='blue')
# ax2.set_xlabel("日期", fontsize=15)
# ax2.set_ylabel("N", fontsize=15)
# ax2.tick_params(labelsize=12)', label='每日新增无症状感染者')
# ax1.set_ylabel('N', fontsize=15)
# ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d\n%Y'))
# ax1.tick_params(labelsize=12)
# ax1.legend(fontsize=12)
plt.figure(figsize = (7,4))
#ax1 = fig.add_subplot(211)
df_city=df_city.loc[(df_city['日期'] >= pd.to_datetime('2022/3/26')) & (df_city['日期'] <= pd.to_datetime('2022/4/26'))] # 筛选出日期小于等于5月1日的数据
plt.plot_date(df_city['日期'], df_city['累计确诊']-df_city['累计治愈出院'], label='Real data', fmt="bo-", markeredgewidth=.004)
# ax1.plot_date(df_city['日期'], infected_counts, 'o-',  color="#D85356", linewidth=3, label='I')
# ax1.plot_date(df_city['日期'], df_city['新增无症状感染者'], 'o-', label='每日新增无症状感染者')
plt.ylabel('N', fontsize=15)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d\n%Y'))
plt.tick_params(labelsize=12)


# ax2 = fig.add_subplot(212)
for i in range(len(infected_counts)):
     infected_counts[i]=infected_counts[i] * 25
df_city=df_city.loc[(df_city['日期'] >= pd.to_datetime('2022/3/26')) & (df_city['日期'] <= pd.to_datetime('2022/4/26'))]  # 筛选出日期小于等于5月1日的数据

plt.plot_date(df_city['日期'], infected_counts, fmt="r+-", markeredgewidth=.5, label='Theoretical results')
plt.xticks(fontsize=9)
plt.yticks(fontsize=10)
#plt.xlabel("t")
plt.rcParams["font.sans-serif"] = "Arial"
plt.legend(loc='best')
#plt.plot(range(num_steps), infected_counts, label='I')
#plt.plot(range(num_steps), recovered_counts, label='R')
with open('result_recovery1.csv', 'w', newline= '') as f:   ################################################# 待改
     writer = csv.writer(f)
     writer.writerow(s_counts)
     writer.writerow(infected_counts)
     writer.writerow(recovered_counts)


y = df_city['累计确诊']-df_city['累计治愈出院']
y_hat = infected_counts
#导入numpy和scipy库
import numpy as np
from scipy.stats import pearsonr

#计算y和y_hat的Pearson相关系数和p值
pearson, pvalue = pearsonr(y, y_hat)
print(f"Pearson correlation coefficient: {pearson:.3f}")
print(f"P-value: {pvalue:.10f}")

#计算y和y_hat的余弦相似度
cosine = np.dot(y, y_hat) / (np.linalg.norm(y) * np.linalg.norm(y_hat))
print(f"Cosine similarity: {cosine:.3f}")

#计算y和y_hat的一阶时间相关系数
#定义一个函数，输入两个向量，输出时间相关系数
def temporal_corr(x, y):
   #计算x和y的长度，应该相等
   n = len(x)
   assert n == len(y)
   #计算x和y的均值
   x_mean = np.mean(x)
   y_mean = np.mean(y)
   #计算x和y的方差
   x_var = np.var(x)
   y_var = np.var(y)
   #计算x和y的协方差
   cov = np.sum((x[:-1] - x_mean) * (y[1:] - y_mean)) / (n - 1)
   #计算时间相关系数
   corr = cov / (np.sqrt(x_var) * np.sqrt(y_var))
   return corr

#调用函数，计算y和y_hat的一阶时间相关系数
temporal = temporal_corr(y, y_hat)
print(f"First order temporal correlation coefficient: {temporal:.3f}")

print(y)
print(y_hat)
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
