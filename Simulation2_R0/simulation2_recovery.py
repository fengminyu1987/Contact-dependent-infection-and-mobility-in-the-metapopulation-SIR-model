import csv
import matplotlib.pyplot as plt
x = []
result = []
csv_file_name = "zhiyu_low.csv"
with open(csv_file_name, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        x.append(float(row['x']))
        result.append(float(row['result']))
plt.plot(x, result,label='low recovery rate', linewidth=3, color='blue')#图例改label，图形状改marker，颜色改color
x = []
result = []
csv_file_name = 'zhiyu_high.csv'
with open(csv_file_name, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        x.append(float(row['x']))
        result.append(float(row['result']))
plt.plot(x, result,label='high recovery rate',linewidth=3, color='red')#图例改label，图形状改marker，颜色改color
plt.xlabel('t')#x轴
plt.ylabel('R0')#y轴
plt.legend()
plt.show()
