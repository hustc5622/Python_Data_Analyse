import os
import pandas as pd
import time
import numpy as np
for i in range(5):
    start=time.time()
    df=pd.read_excel("/Users/cuijie/Desktop/桌面同步文件/我的课题/实验安排及实验数据/数据绘图/烘焙碳10K/DK_0K_0min.xlsx",sheet_name="Ramp 10 °Cmin to 900.00 °C")
    T_raw=df["Temperature"]
    T_raw=T_raw[100:-100]
    sum=0
    for t in T_raw:
        sum+=t
    print(time.time()-start)
    #os.system("sync")
