#烘焙热解碳的实验画图以及对应数据计算
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline


plt.rc('font',family='Times New Roman')
plt.rcParams["font.weight"] = "bold"#加粗字体
plt.rcParams["axes.labelweight"] = "bold"

color_seed=['red','green','pink','purple']

marker_seed=['*','v','d','D',]

marker_size=[10,7,8,7]

Weight_Real=[5.185,4.824,4.950,5.054,5.071,
             5.025,5.065,5.059,4.973,5.060,
             5.086,5.081,5.024,5.064,5.048]

file_seed=['RH-600-5 ',
           'WF-600-5 ',
           'RH-500-5 ',
           'WF-500-5 ',
           'RH-400-5 ',
           
           'WF-400-5 ',
           'RH-300-30',
           'WF-300-30',
           'RH-275-30',
           'WF-275-30',
        
           'RH-250-30',
           'WF-250-30',
           'RH-raw   ',
           'WF-raw   ',
           'FA-raw   ']

File_Name=['~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/DK_600K_5min.xlsx',
           '~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/MF_600K_5min.xlsx',
           '~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/DK_500K_5min.xlsx',
           '~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/MF_500K_5min.xlsx',
           '~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/DK_400K_5min.xlsx',
           
           '~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/MF_400K_5min.xlsx',
           '~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/DK_300K_30min.xlsx',
           '~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/MF_300K_30min.xlsx',
           '~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/DK_275K_30min.xlsx',
           '~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/MF_275K_30min.xlsx',
           
           '~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/DK_250K_30min.xlsx',
           '~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/MF_250K_30min.xlsx',
           '~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/DK_0K_0min.xlsx',
           '~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/MF_0K_0min.xlsx',
           '~/Desktop/实验安排及实验数据/数据绘图/烘焙碳10K/FH_0K_0min.xlsx']
num_lib=[0,1,2,3]

name=[]
Ti=[]
Tb=[]
Tmax=[]
Tmean=[]
Tmax_T=[]
plt.figure(figsize=(12,8),dpi=100)

def draw(num,pos):
        df=pd.read_excel(File_Name[num],sheet_name='Ramp 10 °Cmin to 900.00 °C')
        x1=df['Weight']
        y1=df['Weight Change']
        z1=df['Temperature']
        W_Old=[]
        W_New=[]
        W_C_New=[]
        Y=[]
        T=[]
        for j in range(100,49000):
            W_Old.append((y1[j+1]-100)*x1[0]/100+x1[0])
        for j in range(len(W_Old)):
            W_New.append(W_Old[j]+Weight_Real[num]-x1[0])
        for j in range(len(W_New)):
            W_C_New.append(W_New[j]/Weight_Real[num]*100)
        for j in range(len(W_New)-90):
            Y.append((W_C_New[j]-W_C_New[j+90])/(z1[j+90]-z1[j]))
            T.append(z1[j+100])
        
        
        
        #取点并标记着火点以及燃尽点、最大失重点
        Ti_pos=0
        Tb_pos=0
        flag1=0
        flag2=0
        max_Y=0
        max_X=0
        #min_Y为了画图
        min_Y=0
        for j in range(len(Y)):
            #取了着火点
            if (flag1==0)&(Y[j]>=0.1)&(T[j]>=200):
                Ti.append(T[j])
                temp_str=str(T[j])
                ss='Ti:'+temp_str
                plt.text(x=T[j]-60,y=Y[j]+0.02,s=ss,fontdict={'color':'red','size':15})
                flag1=1
                flag2=1
                Ti_pos=j
            #取了燃尽点
            if (flag2==1)&(T[j]>=300)&(Y[j]<=0.1):
                Tb.append(T[j])
                temp_str=str(T[j])
                ss='Tb:'+temp_str
                plt.text(x=T[j]+10,y=Y[j]+0.02,s=ss,fontdict={'color':'red','size':15})
                Tb_pos=j
                flag2=0
            #取了最大点
            if (max_Y<Y[j])&(T[j]>200):
                max_Y=round(Y[j],3)
                max_X=round(T[j],3)
            #取一个最小值
            if Y[j]<=min_Y:
                min_Y=round(Y[j],2)
                
        Tmax.append(max_Y)
        Tmax_T.append(max_X)
        #取一下文件名字
        
        name.append(file_seed[num])
        
        #求一下平均失重速率
        Tmean.append(Y[Ti_pos]-Y[Tb_pos]/(T[Tb_pos]-T[Ti_pos]))
        
        #间隔取点画图
        YY=[]
        TT=[]
        
        for i in range(1,len(T)):
            if(i%700==0):
                TT.append(T[i])
                YY.append(Y[i])
        
        
        #添加一根指示虚线
        plt.plot([100,700],[0.1,0.1],'k--')
        
        
        #隐藏x轴
        if pos!=len(num_lib)-1:
            ax=plt.gca()
            ax.get_xaxis().set_visible(False)
        
        #改变轴宽度
        ax=plt.gca()
        ax.spines['top'].set_linewidth(2.0)
        ax.spines['bottom'].set_linewidth(2.0)
        ax.spines['left'].set_linewidth(2.0)
        ax.spines['right'].set_linewidth(2.0)
        
        
        
        plt.plot(TT,YY,color=color_seed[pos],
                 linestyle='--',
                 marker=marker_seed[pos],
                 markersize=marker_size[pos],
                 label=file_seed[num])
        
        plt.legend(frameon=False,fontsize=18)
        
        #下面为实现刻度自定义
        step=round((max_Y-min_Y)/4,2)
        a=[min_Y+step,min_Y+step*2,min_Y+step*3,min_Y+step*4]
        
        plt.xticks(size=20)
        plt.yticks(size=20)
        plt.yticks(a)
        return;



for i in range(len(num_lib)):
    plt.subplot(4,1,i+1)
    num=num_lib[i]
    draw(num,i)
    
    
#计算燃烧性能
S=[]
for i in range(len(name)):
    S.append(Tmax[i]*Tmean[i]/Ti[i]/Ti[i]/Tb[i])

ans=pd.DataFrame({'样品名称':name,'着火点':Ti,'燃尽点':Tb,
                  '最大失重速率':Tmax,'最大失重速率对应温度':Tmax_T,'平均失重速率':Tmean,
                  '燃烧性能/S':S})
print(ans)
#ans.to_excel('燃烧特性参数temp.xlsx')

# plt.subplots_adjust(hspace=0)


# plt.text(x=350,y=-0.2,s='Temperature (°C)',fontsize=20)
# plt.text(x=-80,y=0.23,s='DTG (%/°C)',fontsize=20,rotation='vertical')

# plt.show()


