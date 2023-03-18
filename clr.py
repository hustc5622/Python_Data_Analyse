import pandas as pd
while 1:
    print("首先请输入您的文件路径")
    print("请确认文件类型:1.xlsx 2.csv")
    num=input()
    if num==1:
        dirc=input("输入文件路径:")
        df=pd.read_excel(dirc)
    else:
        dirc=input("输入文件路径:")
        df=pd.read_csv(dirc)
    A=df["A"]
    r_lamda=df["B"]
    lamda=[]
    B_lamda=[]
    e_up=0
    e_down=0
    c1=374180000
    c2=14388
    e=2.7182818
    for i in A:
        lamda.append(10000/i)
    for i in range(len(r_lamda)):
        r_lamda[i]=r_lamda[i]/100
    for i in lamda:
        B_lamda.append((c1*(i**(-5)))/(e**(c2/(i*298))-1))
    while 1:
        print("请输入您想要的范围：")
        print("输入下限：")
        lamda_min=float(input())
        print("输入上限：")
        lamda_max=float(input())
        num_min=0
        num_max=0
        for i in range(len(lamda)-1,-1,-1):
            if lamda[i] >= lamda_min:
                num_min=i
                break
        for i in range(len(lamda)-1,-1,-1):
            if lamda[i] >= lamda_max:
                num_max=i
                break
        for i in range(num_max,num_min):
            e_up+=(1-r_lamda[i])*B_lamda[i]*(lamda[i]-lamda[i+1])
            e_down+=B_lamda[i]*(lamda[i]-lamda[i+1])
        print("结果为：")
        print(e_up/e_down)
        print("您要改变上下限吗,输入Y确认,输入N返回文件输入")
        flag=input("输入您的选择：")
        if flag=='N':
            break
    print("您要继续计算吗,输入Y确认,输入N退出程序")
    flag=input("输入您的选择：")
    if flag=='N':
        break