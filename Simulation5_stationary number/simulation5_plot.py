import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#csv_file_list=["1.5_infection0.8.csv", "1.5_infection0.85.csv", "1.5_infection0.9.csv", "1.5_infection0.95.csv", "1.5_infection1.csv", "1.5_infection1.05csv", "1.5_infection1.1.csv", "1.5_infection1.15.csv", "1.5_infection1.2.csv", "1.5_infection1.25.csv", "1.5_infection1.3.csv", "1.5_infection1.35.csv", "1.5_infection1.4.csv", "1.5_infection1.45.csv", "1.5_infection1.5.csv", "1.5_infection1.55.csv", "1.5_infection1.6.csv", "1.5_infection1.65.csv", "1.5_infection1.7.csv", "1.5_infection1.75.csv", "1.5_infection1.8.csv", "1.5_infection1.85.csv", "1.5_infection1.9.csv", "1.5_infection1.95.csv", "1.5_infection2.csv", "1.5_infection2.05csv", "1.5_infection2.1.csv", "1.5_infection2.15.csv", "1.5_infection2.2.csv", "1.5_infection2.25.csv", "1.5_infection2.3.csv", "1.5_infection2.35.csv", "1.5_infection2.4.csv", "1.5_infection2.45.csv", "1.5_infection2.5.csv", "1.5_infection2.55.csv", "1.5_infection2.6.csv"]
plt.figure()
csv_file_list_4=["5_mu_4000-3.00.csv", "5_mu_4000-2.98.csv", "5_mu_4000-2.96.csv", "5_mu_4000-2.94.csv", "5_mu_4000-2.92.csv",
                 "5_mu_4000-2.90.csv", "5_mu_4000-2.88.csv", "5_mu_4000-2.86.csv", "5_mu_4000-2.84.csv", "5_mu_4000-2.82.csv",
                 "5_mu_4000-2.80.csv", "5_mu_4000-2.78.csv", "5_mu_4000-2.76.csv", "5_mu_4000-2.74.csv", "5_mu_4000-2.72.csv",
                 "5_mu_4000-2.70.csv", "5_mu_4000-2.68.csv", "5_mu_4000-2.66.csv", "5_mu_4000-2.64.csv", "5_mu_4000-2.62.csv",
                 "5_mu_4000-2.60.csv", "5_mu_4000-2.58.csv", "5_mu_4000-2.56.csv", "5_mu_4000-2.54.csv", "5_mu_4000-2.52.csv",
                 "5_mu_4000-2.50.csv", "5_mu_4000-2.48.csv", "5_mu_4000-2.46.csv", "5_mu_4000-2.44.csv", "5_mu_4000-2.42.csv",
                 "5_mu_4000-2.40.csv", "5_mu_4000-2.38.csv", "5_mu_4000-2.36.csv", "5_mu_4000-2.34.csv", "5_mu_4000-2.32.csv",
                 "5_mu_4000-2.30.csv", "5_mu_4000-2.28.csv", "5_mu_4000-2.26.csv", "5_mu_4000-2.24.csv", "5_mu_4000-2.22.csv",
                 "5_mu_4000-2.20.csv", "5_mu_4000-2.18.csv", "5_mu_4000-2.16.csv", "5_mu_4000-2.14.csv", "5_mu_4000-2.12.csv",
                 "5_mu_4000-2.10.csv", "5_mu_4000-2.08.csv", "5_mu_4000-2.06.csv", "5_mu_4000-2.04.csv", "5_mu_4000-2.02.csv",
                 "5_mu_4000-2.00.csv"]
sigma = -2.25
x_axis = []
y_axis = []

for file in csv_file_list_4:
    with open(file, mode = 'r') as file:
        x_axis.append(sigma)
        # 初始化该文件内目标列的总和和数量
        sum_columns = 0
        count = 0
        csvreader = csv.reader(file)
        # 读取每一行
        for row in csvreader:
            # 取1600-1700列（Python索引从0开始，所以实际是1599-1699）
            target_columns = row[1899:2000]

            # 计算这些列的值的总和和数量
            for value in target_columns:
                sum_columns += float(value)
                count += 1

        # 计算平均值并添加到y_axis列表
    avg_value = 1/3000 * sum_columns / count
    y_axis.append(avg_value)
    sigma += 0.005
plt.plot(x_axis, y_axis, 'g^-', c="lightgreen", markeredgewidth=.2, label="$r=1/4000$")  # 图例改label，图形状改marker，颜色改color



csv_file_list_5=["5_mu_5000-3.00.csv", "5_mu_5000-2.98.csv", "5_mu_5000-2.96.csv", "5_mu_5000-2.94.csv", "5_mu_5000-2.92.csv",
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
sigma = -2.25
x_axis = []
y_axis = []

for file in csv_file_list_5:
    with open(file, mode = 'r') as file:
        x_axis.append(sigma)
        # 初始化该文件内目标列的总和和数量
        sum_columns = 0
        count = 0
        csvreader = csv.reader(file)
        # 读取每一行
        for row in csvreader:
            # 取1600-1700列（注意Python索引从0开始，所以实际是1599-1699）
            target_columns = row[1899:2000]
            # 计算这些列的值的总和和数量
            for value in target_columns:
                sum_columns += float(value)
                count += 1
        # 计算平均值并添加到y_axis列表
    avg_value = 1/3000 * sum_columns / count
    y_axis.append(avg_value)
    sigma += 0.005
plt.plot(x_axis, y_axis,"bo-", markeredgewidth=.01, label="$r=1/5000$")  # 图例改label，图形状改marker，颜色改color


csv_file_list_6=["5_mu_6000-3.00.csv", "5_mu_6000-2.98.csv", "5_mu_6000-2.96.csv", "5_mu_6000-2.94.csv", "5_mu_6000-2.92.csv",
                 "5_mu_6000-2.90.csv", "5_mu_6000-2.88.csv", "5_mu_6000-2.86.csv", "5_mu_6000-2.84.csv", "5_mu_6000-2.82.csv",
                 "5_mu_6000-2.80.csv", "5_mu_6000-2.78.csv", "5_mu_6000-2.76.csv", "5_mu_6000-2.74.csv", "5_mu_6000-2.72.csv",
                 "5_mu_6000-2.70.csv", "5_mu_6000-2.68.csv", "5_mu_6000-2.66.csv", "5_mu_6000-2.64.csv", "5_mu_6000-2.62.csv",
                 "5_mu_6000-2.60.csv", "5_mu_6000-2.58.csv", "5_mu_6000-2.56.csv", "5_mu_6000-2.54.csv", "5_mu_6000-2.52.csv",
                 "5_mu_6000-2.50.csv", "5_mu_6000-2.48.csv", "5_mu_6000-2.46.csv", "5_mu_6000-2.44.csv", "5_mu_6000-2.42.csv",
                 "5_mu_6000-2.40.csv", "5_mu_6000-2.38.csv", "5_mu_6000-2.36.csv", "5_mu_6000-2.34.csv", "5_mu_6000-2.32.csv",
                 "5_mu_6000-2.30.csv", "5_mu_6000-2.28.csv", "5_mu_6000-2.26.csv", "5_mu_6000-2.24.csv", "5_mu_6000-2.22.csv",
                 "5_mu_6000-2.20.csv", "5_mu_6000-2.18.csv", "5_mu_6000-2.16.csv", "5_mu_6000-2.14.csv", "5_mu_6000-2.12.csv",
                 "5_mu_6000-2.10.csv", "5_mu_6000-2.08.csv", "5_mu_6000-2.06.csv", "5_mu_6000-2.04.csv", "5_mu_6000-2.02.csv",
                 "5_mu_6000-2.00.csv"]
sigma = -2.25
x_axis = []
y_axis = []

for file in csv_file_list_6:
    with open(file, mode = 'r') as file:
        x_axis.append(sigma)
        # 初始化该文件内目标列的总和和数量
        sum_columns = 0
        count = 0
        csvreader = csv.reader(file)
        # 读取每一行
        for row in csvreader:
            # 取1600-1700列（注意Python索引从0开始，所以实际是1599-1699）
            target_columns = row[1899:2000]
            # 计算这些列的值的总和和数量
            for value in target_columns:
                sum_columns += float(value)
                count += 1
        # 计算平均值并添加到y_axis列表
        avg_value = 1/3000 * sum_columns / count
    y_axis.append(avg_value)
    sigma += 0.005

plt.plot(x_axis, y_axis, "r+-", markeredgewidth=.5, label="$r=1/6000$")  # 图例改label，图形状改marker，颜色改color



plt.xlabel("$\sigma$")  # x轴
plt.ylabel('P(S)')  # y轴

plt.legend( )
plt.show( )
