import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y=(1/8)*x
plt.figure(num=1,figsize=(8,5))
plt.plot(x,y,linewidth=10,zorder=1)#zorder表示z轴的覆盖顺序数值越大就越靠上
plt.ylim(-2,2)
#plt.scatter(x,y) scatter是显示出对应的点_散点图

#设定坐标轴到原点
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.7))
#alpha是指不透明度
plt.show()