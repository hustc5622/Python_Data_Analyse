import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.rcParams['font.family']=['Heiti TC']
df1=pd.read_excel('~/Desktop/实验安排及实验数据/数据绘图/数据excel/mx_py_sort.xlsx')
x1=df1["A"]
y1=df1["B"]
x=[]
y=[]
for i in range(x1.size):
    if y1[i]>0:
        x.append(x1[i])
        y.append(y1[i])
plt.figure(figsize=(10,8),dpi=80)#调节画布的大小
labels = x #定义各个扇形的面积/标签
sizes = y #各个值，影响各个扇形的面积
colors1 = [[127/256,106/256,173/256],
           [190/256,182/256,20/256],
           [49/256,197/256,192/256],
           [30/256,155/256,1/256],
           [190/256,100/256,80/256],
           [51/256,51/256,153/256],
           [102/256,153/256,102/256],
           [153/256,51/256,51/256],
           [13/256,102/256,153/256],
           [187/256,102/256,102/256]] #每块扇形的颜色
light = 1.32
colors2 = [[127/256*light,106/256*light,173/256*light],
           [190/256*light,182/256*light,20/256*light],
           [49/256*light,190/256*light,192/256*light],
           [30/256*light,155/256*light,1/256*light],
           [190/256*light,100/256*light,80/256*light],
           [51/256*light,51/256*light,153/256*light],
           [102/256*light,153/256*light,102/256*light],
           [153/256*light,51/256*light,51/256*light],
           [13/256*light,102/256*light,153/256*light],
           [187/256*light,102/256*light,102/256*light],] #每块扇形的颜色
patch, l, p = plt.pie(sizes,
    labels=labels,
    colors=colors1,
    radius=0.9,
    labeldistance = 100,#图例距圆心半径倍距离
    autopct = '%3.2f%%', #数值保留固定小数位
    shadow = False, #无阴影设置
    pctdistance = 0.8,#数值距圆心半径倍数距离
    startangle=90,
    textprops={'fontsize':10,'color':'k'}) 
leg = plt.legend(fontsize = 20, loc=[0.9, 0.2], frameon = False)
plt.pie(sizes,
    labels=labels,
    colors=colors2,
    radius=0.55,
    labeldistance = 100,#图例距圆心半径倍距离
    autopct = '%3.2f%%', #数值保留固定小数位
    shadow = False, #无阴影设置
    pctdistance = 100,
    startangle=90) 
plt.pie([1], radius=0.5, colors='w')
for t in l:
    t.set_size(30)
for t in p:
    t.set_size(20)
plt.axis('equal')
plt.title("sawdust's py-Gc-Ms result",fontsize=20)
#plt.rc('font',family='Times New Roman')
plt.show()