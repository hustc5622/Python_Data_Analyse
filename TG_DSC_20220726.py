import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline

df1=pd.read_excel('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-dk-10k.xlsx',sheet_name="Ramp 10 °Cmin to 900.00 °C")
df2=pd.read_excel('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-dk-20k.xlsx',sheet_name="Ramp 20 °Cmin to 900.00 °C")
df3=pd.read_excel('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-dk-30k.xlsx',sheet_name="Ramp 30 °Cmin to 900.00 °C")
x1=df1["Temperature"]
x2=df2["Temperature"]
x3=df3["Temperature"]
y1=df1["Weight Change"]
y2=df2["Weight Change"]
y3=df3["Weight Change"]


def smooth_xy(x_value: np.ndarray, y_value: np.ndarray):
    model = make_interp_spline(x_value, y_value)
    x_smooth = np.linspace(x_value.min(), x_value.max(), 100)
    y_smooth = model(x_smooth)
    return x_smooth, y_smooth

plt.figure(num=1,figsize=(15,6))
rice_husk_T1=[]
rice_husk_W1=[]
rice_husk_Loss1=[]
rice_husk_T2=[]
rice_husk_W2=[]
rice_husk_Loss2=[]
rice_husk_T3=[]
rice_husk_W3=[]
rice_husk_Loss3=[]

for i in range(100,x1.size-100):
    rice_husk_T1.append(x1[i])
for i in range(100,y1.size-50):
    rice_husk_W1.append(y1[i])
for i in range(len(rice_husk_W1)-50):
    rice_husk_Loss1.append((rice_husk_W1[i]-rice_husk_W1[i+50])/0.08)
x=np.array(rice_husk_T1)
z=np.array(rice_husk_W1)
y=np.array(rice_husk_Loss1)
x,y=smooth_xy(x,y)
plt.plot(x,y,label="10K/min",color='black',linestyle='-')
for i in range(100,x2.size-80):
    rice_husk_T2.append(x2[i])
for i in range(100,y2.size-40):
    rice_husk_W2.append(y2[i])
for i in range(len(rice_husk_W2)-40):
    rice_husk_Loss2.append((rice_husk_W2[i]-rice_husk_W2[i+40])/0.128)
x=np.array(rice_husk_T2)
y=np.array(rice_husk_Loss2)
x,y=smooth_xy(x,y)
plt.plot(x,y,label="20K/min",color='red',linestyle='--')
for i in range(100,x3.size-80):
    rice_husk_T3.append(x3[i])
for i in range(100,y3.size-40):
    rice_husk_W3.append(y3[i])
for i in range(len(rice_husk_W3)-40):
    rice_husk_Loss3.append((rice_husk_W3[i]-rice_husk_W3[i+40])/0.192)
x=np.array(rice_husk_T3)
y=np.array(rice_husk_Loss3)
x,y=smooth_xy(x,y)
plt.plot(x,y,label="30K/min",color='blue',linestyle='-.')


plt.legend(fontsize=20)
# plt.plot([20,20],[0,1],'k--')
# plt.annotate(r'500k',xy=(20,0.25),xycoords='data',xytext=(0,0),textcoords='offset points',
#              fontsize=8)
# plt.plot([36,36],[0,1],'k--')
# plt.annotate(r'660k',xy=(36,0.25),xycoords='data',xytext=(0,0),textcoords='offset points',
#              fontsize=8)

plt.xticks(fontsize=10,rotation=90)
plt.yticks(fontsize=10)

plt.ylabel("DTG(%/°C)",fontsize=20)
plt.xlabel("temperature(°C)",fontsize=20)
plt.show()


