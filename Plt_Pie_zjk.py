from turtle import color
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(7.5,5),dpi=80) #调节画布的大小
labels = ['aa','bb','cc','dd','ee'] #定义各个扇形的面积/标签
sizes = [2, 3, 4, 5, 6] #各个值，影响各个扇形的面积
colors1 = [[127/256,106/256,173/256],
           [190/256,182/256,20/256],
           [49/256,197/256,192/256],
           [30/256,155/256,190/256],
           [220/256,100/256,80/256]] #每块扇形的颜色
light = 1.32
colors2 = [[127/256*light,106/256*light,173/256*light],
           [190/256*light,182/256*light,20/256*light],
           [49/256*light,190/256*light,192/256*light],
           [30/256*light,155/256*light,190/256*light],
           [190/256*light,100/256*light,80/256*light]] #每块扇形的颜色
patch, l, p = plt.pie(sizes,
    labels=labels,
    colors=colors1,
    radius=0.9,
    labeldistance = 100,#图例距圆心半径倍距离
    autopct = '%3.2f%%', #数值保留固定小数位
    shadow = False, #无阴影设置
    pctdistance = 100,#数值距圆心半径倍数距离
    startangle=90) 
leg = plt.legend(fontsize = 20, loc=[0.8, 0.25], frameon = False)
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
plt.show()