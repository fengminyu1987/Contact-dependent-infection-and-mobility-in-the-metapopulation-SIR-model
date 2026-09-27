import csv
import matplotlib.pyplot as plt
import numpy as np
#file_list=['result1.csv','result2.csv','result3.csv','result4.csv','result5.csv']
file_list=['result0.9_recovery.csv','result1_recovery.csv','result1.4_recovery.csv']
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
                plt.plot(labels, s[0::5], color = 'lightgreen', linestyle = ':', linewidth=2.5,label="1.4b")
                plt.plot(labels, i[0::5], color = 'r', linestyle = ':', linewidth=2.5)
                plt.plot(labels, r[0::5], color = 'b', linestyle = ":", linewidth=2.5)

        else:  #为了不显示很多label
            if int == 0:
                plt.plot(labels, s[0::5], color = 'lightgreen', linewidth=2.4, label="0.9b")
                plt.plot(labels, i[0::5], color = 'r', linewidth=2.4)
                plt.plot(labels, r[0::5], color = 'b', linewidth=2.4)
            if int == 1:
                plt.plot(labels, s[0::5], color = 'lightgreen', linestyle = '--', linewidth=2.3, label="b")
                plt.plot(labels, i[0::5], color = 'r', linestyle = '--', linewidth=2.3)
                plt.plot(labels, r[0::5], color = 'b', linestyle = "--", linewidth=2.3)

    int = int + 1

plt.xlabel("t", fontsize = 15)  # 设置横轴标签为"Time"
plt.ylabel("N", fontsize = 15)
plt.legend(fontsize=11,frameon=False,loc="upper left")  # 显示图例
#plt.savefig("Figure_1_recovery.png", dpi=1500) # 保存图像并指定dpi为300

plt.show()
