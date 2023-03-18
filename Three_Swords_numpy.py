import numpy as np
import matplotlib.pyplot as plt
s='''hello
my
world'''
print(s)
s="hello,world"
print(s.split(','))
#[]代表list
actors=['aaa','bbb','ccc']
print(list('abcde'))
a=[]#list可以定义为一个空的列表
a.append(1)
a.append(2)
b=[3,4,5,6,7,8,9]
a+=b
print(a)
print(a[0:3])#左闭右开 [0:-1]-1表示倒数第一个
print(a[0:9:3])#0->9每隔2个取一个数字
aa=(1,2,3,4,5)#元组_一旦被创建就不能被修改
aaa={1:'qq',2:'22'}#类似于map一个key一个value python的括号很关键
s={1,2,3,4,4}#set 集合，不会有重复的元素
print(s)
s='abcd'#str现在是字符串的形式
list(s)
print(s)
print([x**2 for x in range(1,10)])#有一个中括号
abs(-1)#绝对值
#一个函数可以有多个返回值
def f(x):
    return x**2,x**3
print(f(2))
print(type(f(3)))#numpy的切片是引用机制 改变切完片的数值依然会影响原来的数值
a=np.array([0,1,2,3,4,5])
b=a[2:4].copy()#不想应用就得copy
b[0]=10
#花式索引
index=[1,2,-1]
y=a[index]
a=np.arange(0,100,10)
mask=np.array([0,1,1,1,0,0],dtype=bool)#bool数组索引
np.where(a>40)#返回的是一个数组，记录的是index的位置
a=np.array([3,234,234,23,423,423])
b=a.astype(bool)#astype不会改变原有数组 但是a=np.array([],dtype=)就会改变了
print(b)
order=np.argsort(a)#按照从小到大排序 返回数组对应位置的索引 
print(order)
