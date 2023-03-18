import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline
from sympy import true

df1=pd.read_excel('~/Desktop/实验安排及实验数据/数据绘图/数据excel/mf_py_draw_new.xlsx',sheet_name="LibRes")
#df2=pd.read_excel('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mf-20k.xlsx',sheet_name="Ramp 20 °Cmin to 900.00 °C")
#df3=pd.read_excel('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mf-30k.xlsx',sheet_name="Ramp 30 °Cmin to 900.00 °C")
df1[df1['化合物编号 (#)'].isnull()]=0
df1[df1['面积 (Ab*s)'].isnull()]=0
#print(df1.describe())
df1['化合物编号 (#)']=df1['化合物编号 (#)'].astype('int')
df1['面积 (Ab*s)']=df1['面积 (Ab*s)'].astype('int')
x1=df1["面积 (Ab*s)"]
x2=df1["化合物编号 (#)"]
y1=df1["保留时间 (分)"]
p=df1['定性'].astype('int')
n=df1['CAS 编号']
num=[]
area=[]
time=[]
Suitability=[]
for i in range(x1.size):
    if x1[i]>0: 
        area.append(x1[i])
        num.append(x2[i])
        time.append(y1[i])
        Suitability.append(p[i])
plt.figure(num=1,figsize=(15,4))
plt.plot(time,area,color='black')
sum_area=sum(area)

s=pd.DataFrame({'时间':time,'面积':area,'可信度':Suitability,'占总量百分比':area/sum_area*100})
s.drop(s[s['可信度']<60].index,inplace=True)
s.drop(s[s['占总量百分比']<0.5].index,inplace=True)
s=s.sort_values(by='占总量百分比',ascending=False)
percent_sum=sum(s["占总量百分比"])
#print(percent_sum)
s["占总量百分比"]=s["占总量百分比"]/percent_sum*100
s=s.sort_values(by='时间')
print(s.iloc[0,0])
print(s)
plt.xlabel("t/min")
plt.ylabel("relative abundance/%")
# for i in range(0,31):
#     x0=s.iloc[i,0]
#     y0=s.iloc[i,1]
    #plt.annotate(s.iloc[i,0],xy=(x0,y0),xycoords='data',xytext=(-10,20),textcoords='offset points')

plt.show()

#print(area)

#s.to_excel('mx_py.xlsx')