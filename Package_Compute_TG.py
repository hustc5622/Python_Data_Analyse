import pandas as pd
from scipy import optimize as op
import numpy as np
import math as math
import time
name=[]
Range=[]
con_rate=[]
line_squ=[]
e=[]
a=[]
r2=[]
class TG():
    File_name=["/Users/cuijie/Desktop/YJG/PX/p2x8-10k.xls",
            "/Users/cuijie/Desktop/YJG/PX/p4x6-10k.xls",
            "/Users/cuijie/Desktop/YJG/PX/p6x4-10k.xls",
            "/Users/cuijie/Desktop/YJG/PX/p8x2-10k.xls",
            "/Users/cuijie/Desktop/YJG/PX/xyl-10k.xls",
            "/Users/cuijie/Desktop/YJG/PL/pvc-10k.xls"
            ]
    Sheet_name="Ramp 10 °Cmin to 900.00 °C"
    Mark_name=["p2x8-10k",
            "p4x6-10k",
            "p6x4-10k",
            "p8x2-10k",
            "xyl-10k"
                ]
    T_speed=10
    Temperature="Temperature"
    Weight="Weight"
    T_begin=370
    T_end=470
    T_scope=5
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
        for k in range(TG.T_scope):
            T_1=T_1[20:]
            CR=CR[20:]
            temp_T_1=T_1[:]
            temp_CR=CR[:]
            for kk in range(TG.T_scope):
                temp_T_1=temp_T_1[:-20]
                temp_CR=temp_CR[:-20]
                rr,A1,B1,E,A=TG.compute(temp_T_1,temp_CR,pos)
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
        A,B=op.curve_fit(TG.linefunc,T_1,CR)
        A1=A[0]
        B1=A[1]

        CR_fit=T_1[:]
        for i in range(len(CR_fit)):
            CR_fit[i]=CR_fit[i]*A1+B1
        
        rr=TG.goodness_of_fit(CR_fit,CR)
        E=-A1*8.314
        
        aa=math.exp(B1)*TG.T_speed*E/8.314
        return rr,A1,B1,E,aa

    
    #把温度等指标变成行数
    def dododo(i):
        df=pd.read_excel(TG.File_name[i],sheet_name=TG.Sheet_name)
        T_raw=df[TG.Temperature]
        W_raw=df[TG.Weight]
        T_raw=T_raw[50:-50]
        W_raw=W_raw[50:-50]
        W_st=W_raw[50]
        W_end=W_raw[W_raw.size-10]
        j=0
        T_1=[]
        CR=[]
        for T_j in T_raw:
            j=j+1
            if T_j>TG.T_begin-TG.T_scope:
                T_1.append(1/(T_j+273.15))
                CR.append(np.log((-1)*(1/(T_j+273.15))**2*np.log((1-(W_st-W_raw[j])/(W_st-W_end)))))
            if T_j>TG.T_end+TG.T_scope:
                break
        TG.T_scope=int(TG.T_scope/(T_raw[j]-T_raw[j-10]))
        l1,l2,rr,A1,B1,E,A=TG.do_cal(T_1,CR,i)
        name.append(TG.Mark_name[i])
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
        print("算完一个")
        
        

for i in range(5):
    start=time.time()
    TG.dododo(i)
    end=time.time()
    print(end-start)


ans=pd.DataFrame({'样品':name,'Range':Range,'a(%)':con_rate,'Regression equation':line_squ,
                    'E(kj*mol-1)':e,'A(min-1)':a,'R':r2})
ans.to_excel('PC240-360.xlsx')

