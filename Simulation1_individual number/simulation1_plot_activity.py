import csv
import matplotlib.pyplot as plt
import numpy as np
#file_list=['result1.csv','result2.csv','result3.csv','result4.csv','result5.csv']
file_list=['result_activity1.1.csv', "result_activity1.2.csv",'result_activity1.7.csv']
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
                plt.plot(labels, s[0::5], color = 'lightgreen', linestyle = ':', linewidth=2.3)
                plt.plot(labels, i[0::5], color="r", linestyle = ":", linewidth=2.3)
                plt.plot(labels, r[0::5], color = 'b', linestyle = ":", linewidth=2.3)
        else:  #为了不显示很多label
            if int == 0:
                plt.plot(labels, s[0::5], color = 'lightgreen', linewidth=2.2)
                plt.plot(labels, i[0::5], color = 'r', linewidth=2.2)
                plt.plot(labels, r[0::5], color = 'b', linewidth=2.2)
            if int == 1:
                plt.plot(labels, s[0::5], color = 'lightgreen', linestyle = '--', linewidth=2.1)
                plt.plot(labels, i[0::5], color = 'r', linestyle = "--", linewidth=2.1)
                plt.plot(labels, r[0::5], color = 'b', linestyle = "--", linewidth=2.1)
    int = int + 1


# 使用annotate方法在单元格中添加注释，并指定xycoords和textcoords为table对象的属性
# xy参数表示注释箭头的位置，text参数表示注释文本的内容，xytext参数表示注释文本的位置
# arrowprops参数表示注释箭头的样式，prop参数表示注释文本的字体属性
# ax.annotate('', xy=(j, i), xycoords=table.get_celld(), text=colors[index],
# xytext=(0.5, 0.5), textcoords='offset points', ha='center', va='center',
# arrowprops=dict(arrowstyle='-', color=colors[index]), prop=dict(color=colors[index]))

# 使用legend方法添加图例，并指定handles和labels参数为颜色和标签列表中的对应元素
# loc参数表示图例的位置，bbox_to_anchor参数表示图例相对于坐标轴的偏移量
# ax.legend(handles=[plt.plot([], [], marker='o', color=colors[index])[0]], labels=[labels[index]],
# loc='upper left', bbox_to_anchor=(j + 0.2, i - 0.2))
plt.xlabel("t", fontsize = 15)  # 设置横轴标签为"Time"
plt.ylabel("N", fontsize = 15)
plt.legend(fontsize=11,frameon=False,loc="best")  # 显示图例

plt.show()
