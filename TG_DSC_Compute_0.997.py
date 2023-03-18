from symtable import Symbol
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from sympy import *
from scipy import optimize as op

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
df1=pd.read_excel('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mx-30k.xlsx',sheet_name="Ramp 30 °Cmin to 900.00 °C")#df2=pd.read_excel('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mx-20k.xlsx',sheet_name="Ramp 20 °Cmin to 900.00 °C")
#df3=pd.read_excel('~/Desktop/实验安排及实验数据/测试数据/PYORTG-DSC2022_7_22/20220719TG_DSC/wuxiuyi-mx-30k.xlsx',sheet_name="Ramp 30 °Cmin to 900.00 °C")

x1=df1["Temperature"]
#x2=df2["Temperature"]
#x3=df3["Temperature"]
y1=df1["Weight"]
#y2=df2["Weight"]
#y3=df3["Weight"]
z1=df1["1/temperature"]


def Check(l1,l2,flag):
    a1=[]
    a2=[]
    T_1=[]
    #print(y1[30])
    if flag==0:
        for i in range(l1,l2):
                T_1.append(z1[i])
                a2.append(x1[i])
                a1.append((-1)*z1[i]*z1[i]*np.log((1-(y1[30]-y1[i])/(y1[30]-y1[y1.size-10]))))
        for i in range(len(a1)):
            a1[i]=np.log(a1[i])
    elif flag==1:
            T_1.append(z1[i])
            a2.append(x1[i])
            a1.append((-1)*z1[i]*z1[i]*np.log((1-(y1[30]-y1[i])/(y1[30]-y1[y1.size-10]))))
        
    # print('Range')
    # print(x1[l1],"->",x1[l2])
    # print("a")
    # print((y1[30]-y1[l1])/(y1[30]-y1[y1.size-10]),"->",(y1[30]-y1[l2])/(y1[30]-y1[y1.size-10]))

    A,B=op.curve_fit(linefunc,T_1,a1)
    A1=A[0]
    B1=A[1]
    #print("LINE")
    #print("y=",A1,"x+",B1)
    a1_fit=[]
    for i in range(len(T_1)):
        a1_fit.append(A1*T_1[i]+B1)#list不能直接乘呀
    plt.plot(T_1,a1)
    plt.plot(T_1,a1_fit,color='blue')
    rr=goodness_of_fit(a1_fit,a1)
    #print("Fitting rate")
    #print(rr)
    return rr
ii=0
jj=0
flag=0
for i in range(7000,7100):
    for j in range(11100,12201):
        if Check(i,j)>0.997:
            ii=i
            jj=j
            break
    flag=1
    if j!=12200:
        break
    flag=0
if ii==0:
    exit(0)
a1=[]
a2=[]
a3=[]
T_1=[]
for i in range(ii,jj):
        T_1.append(z1[i])
        a2.append(x1[i])
        a1.append((-1)*z1[i]*z1[i]*np.log((1-(y1[30]-y1[i])/(y1[30]-y1[y1.size-10]))))
        #a1[i-12500]=(-0.5)*z1[i]*z1[i]*(1-(1-(y1[30]-y1[i])/(y1[30]-y1[51000]))**(-0.5)) 
        #a2[i-12500]=(-0.2)*z1[i]*z1[i]*(1-(1-(y1[30]-y1[i])/(y1[30]-y1[51000]))**(-0.2)) 
        #a3[i-12500]=(-1)*z1[i]*z1[i]*(1-(1-(y1[30]-y1[i])/(y1[30]-y1[51000]))**(-1))
for i in range(len(a1)):
    a1[i]=np.log(a1[i])

print('Range')
print(x1[ii],"->",x1[jj])
print("a")
print((y1[30]-y1[ii])/(y1[30]-y1[y1.size-10]),"->",(y1[30]-y1[jj])/(y1[30]-y1[y1.size-10]))

A,B=op.curve_fit(linefunc,T_1,a1)
A1=A[0]
B1=A[1]
print("LINE")
print("y=",A1,"x+",B1)
a1_fit=[]
for i in range(len(T_1)):
    a1_fit.append(A1*T_1[i]+B1)#list不能直接乘呀
plt.plot(T_1,a1)
plt.plot(T_1,a1_fit,color='blue')
rr=goodness_of_fit(a1_fit,a1)
print("Fitting rate")
print(rr)


E=-A1*8.314
print("E= ",E)
A=Symbol('A')
print(solve([log(A*8.314*60/(10*E)*1)-B1],[A]))
