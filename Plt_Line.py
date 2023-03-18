from cProfile import label
from hashlib import new
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)#-1到1的50个点
y1=x**2#两个乘号连用就是乘方的意思
y2=2*x+1
plt.figure(num=1,figsize=(7,7))#表明了当前的表格信息


plt.plot(x,y2,label='up')
plt.plot(x,y1,label='down',color='red',linewidth=3,linestyle='dashdot')
plt.legend(loc='lower center')#legend可以将不同曲线的标志显示出来

plt.xlim(-1,2)
plt.ylim(-2,3)#取值范围
plt.xlabel('i am x')
plt.ylabel('i am y')

new_ticks=np.linspace(-1,2,5)
plt.xticks(new_ticks)#改变x轴的数字显示_-1到2分成5份
plt.yticks([-2,-1.8,1.2,3],[r'$really\ good$','good','normal',r'$bad\ \alpha$'])#将y轴对应的数据用文字来显示
#具体的表示可以看表达式 r是正则表达式 有的符号得加\来转译才能表示出来

#gca='get current axis'
ax=plt.gca()
ax.spines['right'].set_color('none')#脊梁指的是图形的边框
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')#设定现在的x和y轴
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))#移动刚才的坐标轴 data表示把x轴移动到y轴对应0的点
ax.spines['left'].set_position(('data',0))
ax.spines['left'].set_position(('outward',-10))#还不明朗具体是什么意思

plt.show()