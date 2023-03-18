import pandas as pd
import numpy as np
#一维series可以用一维列表初始化，可以直接指定索引
s=pd.Series([1,3,5,np.nan,6,8],index=['a','b','c','d','e','f'])
print(s)
print(s.index)
print(s[::2])
#dataframe二维结构
date=pd.date_range('20200801',periods=6)
print(date)
df=pd.DataFrame(np.random.randn(6,4),index=date,columns=list('ABCD'))
print(df)#这时候df会有一个默认的索引
#用字典来创建dataframe二维数组的时候，字典的每个key代表了一列，
#dataframe不要求所有数据类型都相同只要一列的数据相同就行
df2=pd.DataFrame({'A':[1.],'B':[pd.Timestamp('20200801')]})
print(df2)
df2.drop([0],inplace=True)#inplace=True表示直接在愿数据基础上进行修改
df2.to_excel('data.xlsx')#导出excel表格
df=pd.read_excel('~/Desktop/实验安排及实验数据/数据绘图/数据excel/dk-py.xlsx',sheet_name="LibRes")
print(pd.pivot_table(df,index=['化合物编号 (#)'],values=['面积 (Ab*s)'],aggfunc=sum))
#数据透视_大概分析 aggfunc=可以自定一个聚合 计算方式 margins=True表示在末尾显示总和或者就是总的均值

#series层次化索引

s=pd.Series(np.arange(1,10),index=[['a','a','a','b','b','b','c','c','c'],[1,2,3,1,2,3,1,2,3]])
print(s)
print(s['a'])
