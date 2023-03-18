import matplotlib.pyplot as plt
import pandas as pd
from scipy import optimize as op
import os
import numpy as np
import time
import math as math
File_name=[]
Sheet_name=[]
Mark_name=[]
T_speed=[]

Temperature="Temperature"
Weight="Weight"
T_begin=float(0)
T_end=float(0)
T_scope=float(0)

print("欢迎使用本数值计算程序")
print("本程序可以计算动力学参数")
print("首先请输入您的文件路径,可以同时输入多个文件,按回车进行下一个文件输入")
print("您的excel文件第一行应该为对应列的名称,请把多余的内容删除掉")
print("您的文件路径应该按照下面的格式进行对应的修改")
print("例: C:\\\\Users\\\\56307\\\\Desktop\\\\数据\\\\DK300-30#-10k.xls ")
print("每一个文件要有一个对应的sheetname")
print("例: \"Ramp 10 °Cmin to 900.00 °C\" ")
print("最后还需要输入升温速率,这个输入数字即可")


while 1:
    filename=input("请输入文件路径,输入#表示结束输入:")
    if(filename=="#"):
        break
    if(os.path.exists(filename)==False):
        print("文件路径有误,请重新输入")
    else:
        sheetname=input("请输入对应的sheetname:")
        print("请输入升温速率(k/min):")
        t_speed=float(input())
        mark_name=input("请输入当前文件的标记(用于最后结果的输出):")
        File_name.append(filename)
        Sheet_name.append(sheetname)
        T_speed.append(t_speed)
        Mark_name.append(mark_name)


Temperature=input("请输入温度所在列的名称:")
Weight=input("请输入质量所在列的名称:")
print("接下来将对一定温度区间内的数据进行计算,同时支持给定一个范围")
print("例如可以计算200℃ ± 10℃ --->>600℃  ± 10℃  区间的活化能等数值,程序将自动将区间范围内最大的r值对应的情况输出")
print("但是不建议填太大的数值,会导致计算缓慢,最好的范围在5--10")
print("测试中,温度区间取10时,每一个文件大概需要55s来完成计算")
print("请输入起始温度(摄氏度):")
T_begin=float(input())
print("请输入终止温度(摄氏度):")
T_end=float(input())
print("请输入温度范围(摄氏度):")
T_scope=float(input())

print("目前此程序只支持CR法")
print("正在计算中...")

def goodness_of_fit(y_fitting, y_no_fitting):
    sst=0
    ssr=0
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    for i in y_no_fitting:
        sst+=(i-y_mean)**2
    for i in y_fitting:
        ssr+=(i-y_mean)**2
    rr = ssr /sst
    return rr

def linefunc(x,a,b):
    return a*x+b



def do_cal(T_1,CR,pos):
    max_rr=0
    max_A1=0
    max_B1=0
    max_E=0
    max_A=0
    l1=0
    l2=0
    for k in range(2*T_scope):
        T_1=T_1[10:]
        CR=CR[10:]
        temp_T_1=T_1[:]
        temp_CR=CR[:]
        for kk in range(2*T_scope):
            temp_T_1=temp_T_1[:-10]
            temp_CR=temp_CR[:-10]
            rr,A1,B1,E,A=compute(temp_T_1,temp_CR,pos)
            if(rr>max_rr):
                max_rr=rr
                max_A1=A1
                max_B1=B1
                max_E=E
                max_A=A
                l1=1/temp_T_1[0]
                l2=1/temp_T_1[len(temp_T_1)-1]
    return l1,l2,max_rr,max_A1,max_B1,max_E,max_A


def compute(T_1,CR,pos):
    A,B=op.curve_fit(linefunc,T_1,CR)
    A1=A[0]
    B1=A[1]

    CR_fit=T_1[:]
    for i in range(len(CR_fit)):
        CR_fit[i]=CR_fit[i]*A1+B1
    
    rr=goodness_of_fit(CR_fit,CR)
    E=-A1*8.314
    
    aa=math.exp(B1)*T_speed[pos]*E/8.314
    return rr,A1,B1,E,aa


name=[]
Range=[]
con_rate=[]
line_squ=[]
e=[]
a=[]
r2=[]

#把温度等指标变成行数
for i in range(len(File_name)):
    df=pd.read_excel(File_name[i],sheet_name=Sheet_name[i])
    T_raw=df[Temperature]
    W_raw=df[Weight]
    W_st=W_raw[30]
    W_end=W_raw[W_raw.size-10]
    j=0
    T_1=[]
    CR=[]
    print("请根据下面的TG图来判断是否需要修改温度区间")
    time.sleep(3)
    plt.figure()
    plt.plot(T_raw[50:-50],W_raw[50:-50])
    plt.title(Mark_name[i])
    plt.show()
    print("是否要修改温度区间 输入Y表示需要修改 输入N表示不需要")
    if input()=='Y':
        print("请输入起始温度(摄氏度):")
        T_begin=float(input())
        print("请输入终点温度(摄氏度):")
        T_end=float(input())
        print("请输入温度区间:")
        T_scope=float(input())
    print("计算继续进行")
    for T_j in T_raw:
        j=j+1
        if pd.isna(T_j):
            continue
        if T_j>T_begin-T_scope:
            T_1.append(1/(T_j+273.15))
            CR.append(np.log((-1)*(1/(T_j+273.15))**2*np.log((1-(W_st-W_raw[j])/(W_st-W_end)))))
        if T_j>T_end+T_scope:
            break
    T_scope=int(T_scope/(T_raw[j]-T_raw[j-10])/2)
    l1,l2,rr,A1,B1,E,A=do_cal(T_1,CR,i)
    name.append(Mark_name[i])
    num1=round(l1-273.15,2)
    num2=round(l2-273.15,2)
    temp_str=str(num1)+'->'+str(num2)
    Range.append(temp_str)
    j=0
    for TT in T_raw:
        j=j+1
        if TT>l1-273.15:
            num1=round((W_st-W_raw[j])/(W_st-W_end),3)
            break
    j=0
    for TT in T_raw:
        j=j+1
        if TT>l2-273.15:
            num2=round((W_st-W_raw[j])/(W_st-W_end),3)
            break
    temp_str=str(num1)+'->'+str(num2)
    con_rate.append(temp_str)
    A1=round(A1,3)
    B1=round(B1,3)
    temp_str='y='+str(A1)+'x+'+str(B1)
    line_squ.append(temp_str)
    e.append(round(E/1000,2))
    a.append(round(A,2))
    r2.append(round(rr,4))

    ans=pd.DataFrame({'样品':name,'Range':Range,'a(%)':con_rate,'Regression equation':line_squ,
                    'E(kj*mol-1)':e,'A(min-1)':a,'R':r2})
    print("具体结果已经保存在:动力学分析.xlsx中,感谢您的使用,程序将在5秒后退出")
    ans.to_excel('动力学分析.xlsx')
    time.sleep(5)
    