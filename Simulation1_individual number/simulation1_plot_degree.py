import csv
import matplotlib.pyplot as plt
import numpy as np
#file_list=['result1.csv','result2.csv','result3.csv','result4.csv','result5.csv']
file_list=['result_degree6.csv','result_degree8.csv','result_degree10.csv']
plt.figure(figsize = (8, 7))

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
                plt.plot(labels, s[0::5], color = 'lightgreen', linestyle = ':', linewidth=2.3, label="A1")
                plt.plot(labels, i[0::5], color = 'r', linestyle = ':', linewidth=2.3, label="A2")
                plt.plot(labels, r[0::5], color = 'b', linestyle = ":", linewidth=2.3, label="A3")

        else:  #为了不显示很多label
            if int == 0:
                plt.plot(labels, s[0::5], color = 'lightgreen', linewidth=2.2, label="A4")
                plt.plot(labels, i[0::5], color = 'r', linewidth=2.2, label="A5")
                plt.plot(labels, r[0::5], color = 'b', linewidth=2.2, label="A6")
            if int == 1:
                plt.plot(labels, s[0::5], color = 'lightgreen', linestyle = '--', linewidth=2.1, label="A7")
                plt.plot(labels, i[0::5], color = 'r', linestyle = '--', linewidth=2.1,label="A8")
                plt.plot(labels, r[0::5], color = 'b', linestyle = "--", linewidth=2.1,label="A9")

    int = int + 1

plt.xlabel("t", fontsize = 15)  # 设置横轴标签为"Time"
plt.ylabel("N", fontsize = 15)

from matplotlib.lines import Line2D
# legend_elements=[Line2D[0], [0],
#               Line2D[0], [0],
#               Line2D[0], [0],]
#plt.legend(handles=legend_elements, fontsize=11,frameon=False,loc="best", bbox_to_anchor=(1.05,0.9))  # 显示图例
# Create a list of legend handles
legend_handles = [Line2D([0], [0], color=plt.gca().lines[i].get_color(), lw=2, label='A{}'.format(i+1)) for i in range(9)]
plt.legend( fontsize=11,frameon=False,loc="best", bbox_to_anchor=(1.05,0.9), ncol=3)
#plt.savefig('E:\桌面\图\Figure_1_activity.png', bbox_inches="tight")
plt.show()
