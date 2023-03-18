from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import optimize as op
from sympy import *
import math
import copy
#烘焙碳燃烧性能分析




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

Weight_Real=[5.185,4.824,4.950,5.054,5.071,
             5.025,5.065,5.059,4.973,5.060,
             5.086,5.081,5.024,5.064,5.048]

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

def readfile(pos):
    df1=pd.read_excel(File_Name[pos],sheet_name="Ramp 10 °Cmin to 900.00 °C")
    x1=df1['Temperature']
    y1=df1["Weight"]
    z1=df1["1/temperature"]
    file=file_seed[pos]
    return x1,y1,z1,file


def changeline(x1,y1,z1,l1,L1,l2,L2):
    T=[]
    T_1=[]
    CR=[]
    Coa=[]
    a=[]
    a_T=[]
    for i in range(l1,L2):
        T.append(x1[i]+273.15)  #要换成开尔文
    for i in range(len(T)):
        T_1.append(1/T[i])
    for i in range(len(T)):
        CR.append(np.log((-1)*T_1[i]*T_1[i]*np.log((1-(y1[30]-y1[l1+i])/(y1[30]-y1[y1.size-10])))))
    for i in range(len(T)):
        a.append((y1[30]-y1[l1+i])/(y1[30]-y1[y1.size-50]))
    for i in range(len(T)-1000):
        a_T.append((a[i+1000]-a[i])/(T[i+1000]-T[i]))
    for i in range(len(a_T)):
        Coa.append(np.log(a_T[i]/(1-a[i])))
    temp_T_1=copy.deepcopy(T_1)
    temp_CR=copy.deepcopy(CR)
    Coa_T_1=copy.deepcopy(T_1[:-1000])
    for i in range(l1,L1):
        temp_T_1.pop(0)
        temp_CR.pop(0)
        T_1=copy.deepcopy(temp_T_1)
        CR=copy.deepcopy(temp_CR)
        for j in range(l2,L2):
            T_1.pop(len(T_1)-1)
            CR.pop(len(CR)-1)
            #rr,A1,B1,E,A=compute_Coa(Coa_T_1,Coa)
            rr,A1,B1,E,A=compute_CR(T_1,CR)
            if rr>0.1:
                return i,j,rr,A1,B1,E,A
    
def compute_CR(T_1,CR):
    A,B=op.curve_fit(linefunc,T_1,CR)
    A1=A[0]
    B1=A[1]

    CR_fit=[]
    for i in range(len(T_1)):
        CR_fit.append(A1*T_1[i]+B1)
    
    rr=goodness_of_fit(CR_fit,CR)
    
    E=-A1*8.314
    
    
    aa=math.exp(B1)*E*10/8.314
    
    
    return rr,A1,B1,E,aa
    
def compute_Coa(T_1,Coa):
    A,B=op.curve_fit(linefunc,T_1,Coa)
    A1=A[0]
    B1=A[1]

    Coa_fit=[]
    for i in range(len(T_1)):
        Coa_fit.append(A1*T_1[i]+B1)
    
    rr=goodness_of_fit(Coa_fit,Coa)
    
    E=-8.314*A1
    
    aa=math.exp(B1)*10
    
    return rr,A1,B1,E,aa
    
seed=[14]
def do_it():
    name=[]
    Range=[]
    con_rate=[]
    line_squ=[]
    e=[]
    a=[]
    r2=[]
    
    for i in range(len(seed)):
        x1,y1,z1,file=readfile(seed[i])
        for j in range(100,50000):
            if (x1[j]<540)&(x1[j+5]>540):
                T_l1=j
                break
        for j in range(T_l1,50000):
            if (x1[j]<670)&(x1[j+5]>670):
                T_l2=j
                break
        l1,l2,rr,A1,B1,E,A=changeline(x1,y1,z1,T_l1-5,T_l1+5,T_l2-5,T_l2+5)
        name.append(file)
        num1=x1[l1]
        num2=x1[l2]
        temp_str=str(num1)+'-'+str(num2)
        Range.append(temp_str)
        num1=round((y1[30]-y1[l1])/(y1[30]-y1[50000])*100,3)
        num2=round((y1[30]-y1[l2])/(y1[30]-y1[50000])*100,3)
        
        temp_str=str(num1)+'-'+str(num2)
        con_rate.append(temp_str)
        
        rr=round(rr,4)
        A=round(A,3)
        A1=round(A1,3)
        B1=round(B1,3)
        temp_str='y='+str(A1)+'x+'+str(B1)
        line_squ.append(temp_str)
        E=round(E/1000,2)
        e.append(E)
        a.append(A)
        r2.append(rr)

    ans=pd.DataFrame({'样品':name,'Range':Range,'a(%)':con_rate,'Regression equation':line_squ,
                    'E(kj*mol-1)':e,'A(min-1)':a,'R':r2})
    print(ans)
    ans.to_excel('燃烧动力学分析.xlsx')



do_it()

#15800-29200  300-500