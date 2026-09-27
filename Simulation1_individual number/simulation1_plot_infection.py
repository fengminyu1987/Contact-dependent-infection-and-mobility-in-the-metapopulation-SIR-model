import csv
import matplotlib.pyplot as plt
import numpy as np
#file_list=['result1.csv','result2.csv','result3.csv','result4.csv','result5.csv']
file_list=['result1.csv','result2.csv','result4.csv']
plt.figure( )
int=0
# 设置x轴刻度位置，从0到300，每50一个刻度
ticks = range(0, 300)
# 设置x轴刻度标签，从0到1500，每300一个标签
labels = [i * 5 for i in ticks]
for file in file_list:
    with open(file, mode='r') as file:
        reader = csv.reader(file)
        select = 0
        for row in reader:
            if select == 0:
                s = row
                s = [float(a) for a in s]
            if select == 1:
                i = row
                i = [float(a) for a in i]
            if select == 2:
                r = row
                r = [float(a) for a in r]
            select=select+1
        print(file.name)
        if file.name==file_list[-1]: # 等于file_list列表中的最后一个元素

            if int == 2:
                plt.plot(labels, s[0::5], color = 'lightgreen', linestyle = ':', linewidth=2.5)
                plt.plot(labels, i[0::5], color = 'r', linestyle = ':', linewidth=2.5)
                plt.plot(labels, r[0::5], color = 'b', linestyle = ":", linewidth=2.5)
                ## 添加的注释
                plt.text(x = 0,  # 文本x轴坐标
                         y = 400,  # 文本y轴坐标
                         s = '$c=1.1c, 0.9c, 0.8c$',  # 文本内容
                         rotation = 0.5,  # 文字旋转
                         ha = 'left',  # x=2.2是文字的左端位置，可选'center', 'right', 'left'
                         va = 'baseline',  # y=8是文字的低端位置，可选'center', 'top', 'bottom', 'baseline', 'center_baseline'
                         fontdict = dict(fontsize = 10, color = "black",
                                         family = 'cursive',
                                         # 字体,可选'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'
                                         weight = 'light',
                                         # 磅值，可选'light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black'

                                         )  # 字体属性设置
                         )
                #plt.text(x=0, y=300, s="b=1.1b, 0.9b, 0.8b", rotation=0.7, ha='left', fontdict=dict(fontsize=12, color='black',family=))
        else:  #为了不显示很多label
            if int == 0:
                plt.plot(labels, s[0::5], color = 'lightgreen', label = 'S', linewidth=2.5)
                plt.plot(labels, i[0::5], color = 'r', label = 'I', linewidth=2.5)
                plt.plot(labels, r[0::5], color = 'b', label = 'R', linewidth=2.5)
            if int == 1:
                plt.plot(labels, s[0::5], color = 'lightgreen', linestyle = '--', linewidth=2.5)
                plt.plot(labels, i[0::5], color = 'r', linestyle = '--', linewidth=2.5)
                plt.plot(labels, r[0::5], color = 'b', linestyle = "--", linewidth=2.5)

    int = int + 1

plt.xlabel("t", fontsize = 15)  # 设置横轴标签为"Time"
plt.ylabel("N", fontsize = 15)
plt.legend(fontsize=11,frameon=False,loc="best")  # 显示图例

plt.show()
