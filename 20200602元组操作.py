'''''
元组数据不支持修改，只支持查找
'''''
t1 = ('aa', 'bb', 'cc', 'bb')
#1. 下标
print(t1[0])#aa

#2. index()
print(t1.index('bb'))#1
#print(t1.index('bbb'))#报错

#3. count()
print(t1.count('aa'))#1
print(t1.count('aaa'))#0

#4. len()
print(len(t1)) #4

print('元组数据修改(元组里的数组)----------------------------------------')
t1 = ('aa', 'bb', 'cc', 'bb')
t2=('aa','bb',['cc','dd'])
print(t2[2])#['cc', 'dd']
print(t2[2][0])#cc
t2[2][0]='Tom'
print(t2)#('aa', 'bb', ['Tom', 'dd'])
