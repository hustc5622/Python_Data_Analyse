
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import optimize as op
from sympy import *
#计算原料(DK\MF\MX)的10，20，30K/min升温速率下的热解动力学

# #################################拟合优度R^2的计算######################################
def __sst(y_no_fitting):
    """
    计算SST(total sum of squares) 总平方和
    :param y_no_predicted: List[int] or array[int] 待拟合的y
    :return: 总平方和SST
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list =[(y - y_mean)**2 for y in y_no_fitting]
    sst = sum(s_list)
    return sst


def __ssr(y_fitting, y_no_fitting):
    """
    计算SSR(regression sum of squares) 回归平方和
    :param y_fitting: List[int] or array[int]  拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 回归平方和SSR
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list =[(y - y_mean)**2 for y in y_fitting]
    ssr = sum(s_list)
    return ssr


def __sse(y_fitting, y_no_fitting):
    """
    计算SSE(error sum of squares) 残差平方和
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 残差平方和SSE
    """
    s_list = [(y_fitting[i] - y_no_fitting[i])**2 for i in range(len(y_fitting))]
    sse = sum(s_list)
    return sse


def goodness_of_fit(y_fitting, y_no_fitting):
    """
    计算拟合优度R^2
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 拟合优度R^2
    """
    SSR = __ssr(y_fitting, y_no_fitting)
    SST = __sst(y_no_fitting)
    rr = SSR /SST
    return rr

def linefunc(x,a,b):
    return a*x+b

File_Name=['~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mx-10k.xlsx',
           '~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mx-20k.xlsx',
           '~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mx-30k.xlsx',
           '~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mf-10k.xlsx',
           '~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mf-20k.xlsx',
           
           '~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mf-30k.xlsx',
           '~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-dk-10k.xlsx',
           '~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-dk-20k.xlsx',
           '~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-dk-30k.xlsx',
           ]
Sheet_name=['Ramp 10 °Cmin to 900.00 °C',
            'Ramp 20 °Cmin to 900.00 °C',
            'Ramp 30 °Cmin to 900.00 °C',
            ]

Name_seed=['mx-10k',
           'mx-20k',
           'mx-30k',
           'mf-10k',
           'mf-20k',
           
           'mf-30k',
           'dk-10k',
           'dk-20k',
           'dk-30k',
           ]

Speed_seed=[10,20,30]

def readfile(pos):
    df1=pd.read_excel(File_Name[pos],Sheet_name[pos%3])
    x1=df1['Temperature']
    y1=df1["Weight"]
    z1=df1["1/temperature"]
    return x1,y1,z1,Name_seed[pos]


def changeline(x1,y1,z1,l1,L1,l2,L2,pos):
    T=[]
    T_1=[]
    CR=[]
    for i in range(l1,l2):
        T.append(x1[i]+273.15)  #要换成开尔文
    for i in range(len(T)):
        T_1.append(1/T[i])
    for i in range(len(T)):
        CR.append(np.log((-1)*z1[i]*z1[i]*np.log((1-(y1[30]-y1[i])/(y1[30]-y1[y1.size-10])))))
    temp_T_1=T_1
    temp_CR=CR
    for i in range(l1,L1):
        temp_T_1.pop(0)
        temp_CR.pop(0)
        T_1=temp_T_1
        CR=temp_CR
        for j in range(l2,L2):
            T_1.append(z1[j])
            CR.append(np.log((-1)*z1[j]*z1[j]*np.log((1-(y1[30]-y1[j])/(y1[30]-y1[y1.size-10])))))
            rr,A1,B1,E,A=compute(T_1,CR,pos)
            if rr>0.95:
                return i,j,rr,A1,B1,E,A
    

def compute(T_1,CR,pos):
    A,B=op.curve_fit(linefunc,T_1,CR)
    A1=A[0]
    B1=A[1]

    CR_fit=[]
    for i in range(len(T_1)):
        CR_fit.append(A1*T_1[i]+B1)
        
    rr=goodness_of_fit(CR_fit,CR)
    E=-A1*8.314
    
    A=Symbol('A')
    aa=solve([np.log(A*8.314/Speed_seed[pos]/E)-B1],[A])
    
    
    return rr,A1,B1,E,aa


seed=[0,3,6]

def do_it():
    name=[]
    Range=[]
    con_rate=[]
    line_squ=[]
    e=[]
    a=[]
    r2=[]
    
    #for i in range(len(seed)):
    x1,y1,z1,file=readfile(seed[0])
    l1,l2,rr,A1,B1,E,A=changeline(y1,z1,11900,12500,27500,28000,seed[0])
    name.append(file)
    num1=x1[l1]
    num2=x1[l2]
    temp_str=str(num1)+'->'+str(num2)
    Range.append(temp_str)
    num1=(y1[30]-y1[l1])/(y1[30]-y1[50000])
    num2=(y1[30]-y1[l2])/(y1[30]-y1[50000])
    temp_str=str(num1)+'->'+str(num2)
    con_rate.append(temp_str)
    
    temp_str='y='+str(A1)+'x+'+str(B1)
    line_squ.append(temp_str)
    e.append(E)
    a.append(A)
    r2.append(rr)

    ans=pd.DataFrame({'样品':name,'Range':Range,'a(%)':con_rate,'Regression equation':line_squ,
                    'E(kj*mol-1)':e,'A(min-1)':a,'R':r2})
    print(ans)
    #ans.to_excel('动力学分析0823.xlsx')
