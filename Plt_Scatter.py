import matplotlib.pyplot as plt
import numpy as np

n=1024
x=np.random.normal(0,1,n)#平均值是0，方差是1
y=np.random.normal(0,1,n)
t=np.arctan2(y,x)#颜色的计算公式

plt.scatter(x,y,s=75,c=t,alpha=0.5)

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.xticks(())
plt.yticks(())#没写就是全部隐藏
plt.legend()
plt.show()