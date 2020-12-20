import pandas as pd
from pylab import mpl

# 读取数据
file = open(r'D:\数据分析\链家北京租房数据.csv')
file_data = pd.read_csv(file)
# 删除重复值和缺失值
file_data = file_data.drop_duplicates()  # 删除重复值
file_data = file_data.dropna()  # 删除缺失值
# 将“户型”一列统一调整为“x室x厅”格式
temp_list = []
for i in file_data['户型']:
    temp = i.replace('房间', '室')
    temp_list.append(temp)
file_data['户型'] = temp_list

temp_list = []
for i in file_data['户型']:
    temp = i.replace('卫', '厅')
    temp_list.append(temp)
file_data['户型'] = temp_list
# 将“面积”一列调整为数值格式
temp_list = []
for i in file_data['面积(㎡)']:
    temp = i.strip('平米')
    temp = float(temp)
    # temp = i.replace('平米', '')
    temp_list.append(temp)
file_data['面积(㎡)'] = temp_list
print("file_data['面积(㎡)'].dtype:\n", file_data['面积(㎡)'].dtype)
# 使用箱形图检查“面积”和“价格”列中是否存在异常数据
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置显示中文字体
mpl.rcParams['axes.unicode_minus'] = False  # 设置正常显示符号
# file_data_box = file_data.boxplot(column=['面积(㎡)', '价格(元/月)'])
# print(file_data_box)
# 使用“区域”和“小区名称”新增“位置”一列，形如“北京市xx区xx”
file_data["位置"] = "北京市" + file_data['区域'] + "区" + file_data['小区名称']
print(file_data)

file_data["每平米价格"] = file_data["价格(元/月)"] / file_data["面积(㎡)"]
print("每平米价格的最大值", file_data["价格(元/月)"].max())
print("每平米价格的最小值", file_data["价格(元/月)"].min())
print("每平米价格的平均值", file_data["价格(元/月)"].mean())
file_data_cutbyarea = pd.cut(x=file_data["面积(㎡)"], bins=10)
print("file_data_cutbyarea\n:", file_data_cutbyarea)
file_data_groupby = file_data.groupby(by='户型')
for i in file_data_groupby:
    print(i[0])
'''
import numpy as np
temp_list = []
for i in file_data_groupby:
    temp_list.append(i[0])
total = []
for j in temp_list:
    total.append(str(dict([x for x in file_data_groupby])[j].shape[0]))
file_data_price = file_data_groupby["价格(元/月)"].agg([np.max, np.min, np.mean])
file_data_price["户型数量"] = total
print(file_data_price)

import numpy as np

file_data_groupbyhaidian = file_data.groupby(by='区域')
temp_list = []
for i in file_data_groupbyhaidian:
    temp_list.append(i[0])
total = []
for j in temp_list:
    total.append(str(dict([x for x in file_data_groupbyhaidian])[j].shape[0]))
file_data_groupbyhaidian = file_data_groupbyhaidian["价格(元/月)"].agg([np.max, np.min, np.mean])
file_data_groupbyhaidian["房源数量"] = total
print(file_data_groupbyhaidian)

# 按面积画饼图
import matplotlib.pyplot as plt

bins = [0, 50, 60, 70, 90, 120, 140, 160, 1200]
area_divide = pd.cut(list(file_data["面积(㎡)"]), bins=bins)
area_divide_data = area_divide.describe()
area_per = area_divide_data['freqs'].values * 100
print(area_divide_data)
labels = ['(0, 50]', '(50, 60]', '(60, 70]', '(70, 90]', '(90, 120]',
          '(120, 140]', '(140, 160]', '(160, 1200]']
plt.pie(area_per, labels=labels, autopct='%.2f %%', labeldistance=1.2, startangle=90, pctdistance=0.7)
plt.show()

# 将“价格”按不同的区间绘制为饼图
import matplotlib.pyplot as plt

bins = [0, 4000, 5000, 6000, 7000, 8000, 10000, 12000, 15000, 150000]
area_divide = pd.cut(list(file_data["价格(元/月)"]), bins=bins)
area_divide_data = area_divide.describe()
area_per = area_divide_data['freqs'].values * 100
print(area_divide_data)

labels = ['(0, 4000]', '(4000, 5000]', '(5000, 6000]', '(6000, 7000]', '(7000, 8000]', '(8000, 10000]', '(10000, 12000]',
          '(12000, 15000]', '(15000, 150000]']
plt.pie(area_per, labels=labels, autopct='%.2f %%', labeldistance=1.2, startangle=90, pctdistance=0.7)
plt.show()
'''
# 将“户型”一列调整为x室
temp_list = []
for i in file_data['户型']:
    temp = i[:2]
    temp_list.append(temp)
file_data['户型'] = temp_list
print(file_data)
# 将户型分类
file_data_groupby = file_data.groupby(by='户型')
for i in file_data_groupby:
    print(i[0])

import numpy as np


# 定义函数，用于计算各类户型的数量
def all_house(arr):
    arr = np.array(arr)
    key = np.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result[k] = v
    return result


# 获取户型数据
house_array = file_data['户型']
house_info = all_house(house_array)
print("house_info:\n", house_info)
# 获取区域数据
area_array = file_data['区域']
area_info = all_house(area_array)
print("area_info:\n", area_info)
'''
# 将“户型”按x室绘制为饼图
import matplotlib.pyplot as plt

labels = ['0室', '1室', '2室', '3室', '4室', '5室', '6室', '7室', '8室', '9室']
plt.pie(house_info.values(), labels=labels, autopct='%.2f %%', labeldistance=1.2, startangle=90, pctdistance=0.7)
plt.show()

# 将“区域”按x室和区域（如海淀）分组的房源数量和平均租金信息 绘制为条形图、折线图。
import matplotlib.pyplot as plt

df_area = pd.DataFrame({'区域': file_data['区域'].unique(),
                        '每平米价格': [0] * 13,
                        '房源数量': [0] * 13,
                        '总价格': [0] * 13,
                        '总面积': [0] * 13})
df_area['总面积'] = file_data['面积(㎡)'].groupby(file_data['区域']).sum().values
df_area['总价格'] = file_data['价格(元/月)'].groupby(file_data['区域']).sum().values
df_area['每平米价格'] = round(df_area['总价格'] / df_area['总面积'], 2)
df_area['房源数量'] = area_info.values()
print(file_data)
print(df_area)

num = df_area['房源数量']
price = df_area['每平米价格']
l = [i for i in range(13)]
plt.rcParams['font.sans-serif'] = ['SimHei']
lx = df_area['区域']
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(l, price, 'or-', label='价格')
for i, (_x, _y) in enumerate(zip(l, price)):
    plt.text(_x, _y, price[i], color='b', fontsize=10)
ax1.set_ylim([0, 200])
ax1.set_ylabel('价格')
plt.legend(prop={'family': 'SimHei', 'size': 8}, loc='upper left')
ax2 = ax1.twinx()
plt.bar(l, num, alpha=0.3, label='数量')
ax2.set_ylabel('数量')
ax2.set_ylim([0, 2000])
plt.legend(prop={'family': 'SimHei', 'size': 8}, loc='upper right')
plt.xticks(l, lx)
plt.show()
'''
# 将“户型”按x室和区域（如海淀）分组的房源数量和平均租金信息 绘制为条形图、折线图。
import matplotlib.pyplot as plt

df_kind = pd.DataFrame({'户型': file_data['户型'].unique(),
                        '每平米价格': [0] * 10,
                        '房源数量': [0] * 10,
                        '总价格': [0] * 10,
                        '总面积': [0] * 10})
df_kind['总面积'] = file_data['面积(㎡)'].groupby(file_data['户型']).sum().values
df_kind['总价格'] = file_data['价格(元/月)'].groupby(file_data['户型']).sum().values
df_kind['每平米价格'] = round(df_kind['总价格'] / df_kind['总面积'], 2)
df_kind['房源数量'] = house_info.values()
print(file_data)
print(df_kind)

num = df_kind['房源数量']
price = df_kind['每平米价格']
l = [i for i in range(10)]
plt.rcParams['font.sans-serif'] = ['SimHei']
lx = df_kind['户型']
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(l, price, 'or-', label='价格')
for i, (_x, _y) in enumerate(zip(l, price)):
    plt.text(_x, _y, price[i], color='b', fontsize=10)
ax1.set_ylim([0, 200])
ax1.set_ylabel('价格')
plt.legend(prop={'family': 'SimHei', 'size': 8}, loc='upper left')
ax2 = ax1.twinx()
plt.bar(l, num, alpha=0.3, label='数量')
ax2.set_ylabel('数量')
ax2.set_ylim([0, 2000])
plt.legend(prop={'family': 'SimHei', 'size': 8}, loc='upper right')
plt.xticks(l, lx)
plt.show()
