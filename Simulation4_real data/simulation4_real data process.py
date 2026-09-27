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

path = '上海2022年3月疫情统计数据.xlsx'
df_city = pd.read_excel(path)

# 将日期列转换为日期类型
df_city['日期'] = pd.to_datetime(df_city['日期'], format='%Y年%m月%d日')

# 选择3月1日到5月10日的数据
start_date = pd.Timestamp('2022-03-01')
end_date = pd.Timestamp('2022-05-10')
df_city = df_city[(df_city['日期'] >= start_date) & (df_city['日期'] <= end_date)]

print(df_city)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
plt.tick_params(labelsize=15)
ax.plot_date(df_city['日期'].iloc[0:45], df_city['新增确诊病例'].iloc[0:45], 'o-')
plt.ylabel('每日新增确诊病例',fontsize=15)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d\n%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))
plt.show()


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
plt.tick_params(labelsize=15)
ax.plot_date(df_city['日期'], df_city['新增确诊病例'], 'o-')
plt.ylabel('每日新增确诊病例',fontsize=15)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d\n%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=4))
plt.show()


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
plt.tick_params(labelsize=15)
ax.plot_date(df_city['日期'].iloc[0:40], df_city['新增无症状感染者'].iloc[0:40], 'o-')
plt.ylabel('每日新增易感染者',fontsize=15)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d\n%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))
plt.show()


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
plt.tick_params(labelsize=15)
ax.plot_date(df_city['日期'], df_city['新增无症状感染者'], 'o-')
plt.ylabel('每日新增易感染者',fontsize=15)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d\n%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=4))
plt.show()


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
plt.tick_params(labelsize=15)
ax.plot_date(df_city['日期'], df_city['累积无症状'], 'o-')
plt.ylabel('累计易感染者',fontsize=15)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d\n%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=4))
plt.show()

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
plt.tick_params(labelsize=15)
ax.plot_date(df_city['日期'], df_city['累计确诊'], 'o-')
plt.ylabel('累计确诊病例数',fontsize=15)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d\n%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=4))

plt.show()