import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline
import matplotlib.gridspec as gri

def smooth_xy(x_value: np.ndarray, y_value: np.ndarray):
    model = make_interp_spline(x_value, y_value)
    x_smooth = np.linspace(x_value.min(), x_value.max(), 100)
    y_smooth = model(x_smooth)
    return x_smooth, y_smooth
def draw(loc,sheet,column,line,num,title):
    df=pd.read_excel(loc,sheet_name=sheet)
    x1=df["Temperature"]
    #y1=df["Weight"]
    y2=df["Weight Change"]
    y3=df["Heat Flow"]
    
    plt.subplot(column,line,num+1)
    plt.title(title,fontsize=12)
    T=[]
    for i in range(50,x1.size-50):
        T.append(x1[i])
    W=[]
    for i in range(50,x1.size-50):
        W.append(y2[i])
    W_C=[]
    if(i%3==0):
        index=0.08
    elif(i%3==1):
        index=0.128
    elif(i%3==2):
        index=0.192
    for i in range(50,x1.size-50):
        W_C.append((y2[i]-y2[i+50])/index)
    H_F=[]
    for i in range(50,x1.size-50):
        H_F.append(y3[i])
    
    
    
    x=np.array(T)
    y=np.array(W)
    #x,y=smooth_xy(x,y)
    plt.plot(x,y,label="TG",color='black',linestyle='-')
    if(num==8):
        plt.legend(bbox_to_anchor=(1.37,0.1),frameon=False)
    plt.ylabel("TG(%)",fontsize=10)
    plt.xlabel("temperature(°C)",fontsize=10)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    
    
    
    ax2=plt.twinx()
    #ax3=plt.twinx()
    #x=np.array(T)
    y=np.array(H_F)
    #x,y=smooth_xy(x,y)
    ax2.plot(x,y,label="DSC",color='red',linestyle='--')
    ax2.set_ylabel("Heat Flow(mW)",color='red')
    #x=np.array(T)
    #y=np.array(W_C)
    #x,y=smooth_xy(xDSC
    # ax3.plot(x,y,label="DSC",color='blue',linestyle='-.')
    # ax3.set_ylabel("DTG(%/min)",color='blue')
    if(num==8):
        plt.legend(bbox_to_anchor=(1.4,0),frameon=False)
    # plt.plot([20,20],[0,1],'k--')
    # plt.annotate(r'500k',xy=(20,0.25),xycoords='data',xytext=(0,0),textcoords='offset points',
    #              fontsize=8)
    # plt.plot([36,36],[0,1],'k--')
    # plt.annotate(r'660k',xy=(36,0.25),xycoords='data',xytext=(0,0),textcoords='offset points',
    #              fontsize=8)

    



#main
loc=[]
loc.append('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-dk-10k.xlsx')
loc.append('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-dk-20k.xlsx')
loc.append('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-dk-30k.xlsx')
loc.append('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mx-10k.xlsx')
loc.append('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mx-20k.xlsx')
loc.append('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mx-30k.xlsx')
loc.append('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mf-10k.xlsx')
loc.append('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mf-20k.xlsx')
loc.append('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mf-30k.xlsx')



sheet=[]
sheet.append('Ramp 10 °Cmin to 900.00 °C')
sheet.append('Ramp 20 °Cmin to 900.00 °C')
sheet.append('Ramp 30 °Cmin to 900.00 °C')

title=[]
title+=['rice husk 10k/min','rice husk 20k/min','rice husk 30k/min']
title+=['sawdust 10k/min','sawdust 20k/min','sawdust 30k/min']
title+=['wood flour 10k/min','wood flour 20k/min','wood flour 30k/min']

plt.figure(figsize=(16,8))
for i in range(9):
    draw(loc[i],sheet[i%3],3,3,i,title[i])

# plt.annotate('ricehusk',xy=(2,4),xycoords='data',xytext=(0,0),textcoords='offset points',fontsize=6)
# plt.annotate('sawdust',xy=(2,3),xycoords='data',xytext=(0,0),textcoords='offset points',fontsize=6)
# plt.annotate('woodflour',xy=(2,2),xycoords='data',xytext=(0,0),textcoords='offset points',fontsize=6)
plt.subplots_adjust(left=None,right=None,bottom=None,top=None,wspace=0.5,hspace=0.5)
plt.rc('font',family='Times New Roman')
plt.show()