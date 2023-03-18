from turtle import color, position
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y=2*x+1
plt.figure(num=1,figsize=(8,5))
plt.plot(x,y)
#plt.scatter(x,y) scatter是显示出对应的点_散点图

#设定坐标轴到原点
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

x0=1
y0=2*x0+1
plt.scatter(x0,y0,s=50,color='red')#把这个点显示出来了 s=size
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)#'k--'k表示black --表示虚线

plt.annotate(r'$2x+1=3$',xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',
             fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0.2'))
#xycoords表示的被注释点的坐标属性，通常为data xytext表示文字相对于点的相对位置 textcoords表示点还是像素(pixels)
#arrowprops后面表示箭头的属性，详情见https://www.imooc.com/article/295812

plt.text(-3.7,3,r'$This\ is\ the\ some\ text.\ \mu\ \sigma^i\ \alpha_t$')
#sigma_i表示右下角标 ^是右上角标

plt.show()