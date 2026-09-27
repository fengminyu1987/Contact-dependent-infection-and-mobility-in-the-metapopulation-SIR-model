import geopandas as gpd  # 要下载依赖库：Rtree GDAL pyproj Shapely Fiona 我的python版本支持的：cp38
import matplotlib.pyplot as plt
import pandas as pd

# 1. 加载地理边界数据
shp_path = "上海各区县shp文件数据/Shanghai.shp"
map_data = gpd.read_file(shp_path)

# 2. 连接数值数据
data = {
    "District": ["虹口区", "长宁区", "崇明县", "杨浦区", "普陀区", "宝山区", "黄浦区", "奉贤县", "徐汇区", "青浦区",
                  "金山区", "静安区", "嘉定区", "松江区", "闵行区", "浦东新区", "南汇县", "卢湾区", "闸北区"],
    "Value": [647601.00, 684600.00, 672900.00, 1242548.00, 899400.00, 2271900.00, 662030.00,
              1126300.00, 1113078.00, 1265600.00, 622776.00, 975700.00, 1893400.00, 1909713.00,
              2688800.00, 5782000.00, 0, 0, 0]
}
data_df = pd.DataFrame(data)

# 3. 合并地理边界数据和数值数据
merged_data = map_data.merge(data_df, left_on="NAME", right_on="District")

# 4. 设置默认字体为支持中文显示的字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 5. 绘制Choropleth地图
fig, ax = plt.subplots(figsize=(10, 10))
# merged_data.plot(column="Value", cmap="BuGn", linewidth=0.8, ax=ax, edgecolor="0.8")
merged_data.plot(column="Value", cmap="YlGnBu", linewidth=0.8, ax=ax)
#plt.title("上海各区县 Choropleth 地图")
plt.axis("off")

# 6. 添加地区标签
# for x, y, label in zip(merged_data.geometry.centroid.x, merged_data.geometry.centroid.y, merged_data["District"]):
#     ax.text(x, y, label, fontsize=8, ha='center', va='center')

# 7. 添加颜色图例
# 设置全局的字体参数
plt.rcParams['font.sans-serif'] = ['Arial']
sm = plt.cm.ScalarMappable(cmap="YlGnBu")
sm.set_array(merged_data["Value"])
cbar = plt.colorbar(sm, label="Level of disease", fraction=0.38, aspect=22)
cbar.set_label("Level of disease", fontsize=10) # 标签字体大小
cbar.ax.tick_params(labelsize=9) # 刻度字体大小
offset_text = cbar.ax.yaxis.get_offset_text() # 科学计数法1e6字体大小
offset_text.set_fontsize(9)
#8. 添加连线
# x_coords = []
# y_coords = []
#
# for i in range(len(merged_data)):
#     if merged_data["Value"][i] >= 0:
#         centroid = merged_data.geometry.centroid[i]
#         x_coords.append(centroid.x)
#         y_coords.append(centroid.y)
#
# plt.plot(x_coords, y_coords, color='gray', linewidth=1)
plt.savefig("shanghai.png", dpi=1500) # 保存图像并指定dpi为300
plt.show()
