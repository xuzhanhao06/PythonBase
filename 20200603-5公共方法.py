str1 = 'abcdefg'
list1 = [10, 20,30, 40, 50]
t1 = (10,20,30,40,50)
s1 = {10,20,30,40,50}
dict1 = {'name':'TOM','age': 18}

print('-'*10+'len()'+'-'*10)
print(len(str1))#7
print(len(list1))#5
print(len(t1))#5
print(len(s1))#5
print(len(dict1))#2

print('-'*10+'del(目标)或者del 目标'+'-'*10)
#del(list1)
#print(list1)#报错
del(list1[0])
print(list1)#[20, 30, 40, 50]

#del dict1
#print(dict1)#报错
del dict1['name']
print(dict1)#   {'age': 18}

print('-'*10+'del(目标)或者del 目标'+'-'*10)
str1 = 'abcdefg'
list1 = [10, 20,30, 40, 50]
#max()
print(max(str1))#g
print(max(list1))#50
#min()
print(min(str1))#a
print(min(list1))#10

print('-'*10+'range()'+'-'*10)
for i in range(1,10,1):
    print(i,end=' ')#1 2 3 4 5 6 7 8 9
print()
for i in range(1,10):
    print(i, end=' ')  #1 2 3 4 5 6 7 8 9
print()
for i in range(1,10,2):
    print(i, end=' ')#1 3 5 7 9
print()
for i in range(10):
    print(i, end=' ')  #0 1 2 3 4 5 6 7 8 9
'''''
如果不写开始，默认从0开始
如果不写步长，默认为1,
'''''

print('-'*10+'enumerate(可遍历对象,start=0)'+'-'*10)
list1=['a','b','c','d','e']
for i in enumerate(list1,start=1):
    print(i)

'''''
(1, 'a')
(2, 'b')
(3, 'c')
(4, 'd')
(5, 'e')
'''''
print('----tuple()-------------')

list1 = [10,20,30,20,40,50]
s1={100,300,200,500}
t1 =('a','b','c','d','e' )
#tuple(): 转换成元组
print(tuple(list1))#(10, 20, 30, 20, 40, 50)
#list():转换成列表
print(list(s1))#[200, 100, 500, 300]
print(list(t1))#['a', 'b', 'c', 'd', 'e']
#set()：转换成集合,去重，不支持下标
print(set(list1))#{40, 10, 50, 20, 30}   去除了重复的
print(set(t1))#{'b', 'd', 'a', 'c', 'e'}