str1 ='aa'
str2="bb"
list1 = [1, 2]
list2 = [10, 20]
t1=(1,2)
t2 = (10,20)
dict1={'name':'Python'}
dict2={'age': 30}

print('------- +: 合并 -----------------')
print(str1+str2)#aabb
print(list1+list2)#[1, 2, 10, 20]
print(t1+t2)#(1, 2, 10, 20)
#print(dict1+dict2)#报错！！！  不支持合并

print('------- *: 复制 -----------------')
str1 ='a'
list1 = ['hello ' ]
t1 = ('world',)

print(str1*5)#aaaaa
#打印10个-
print('-'*10)#----------
print(list1*5)#['hello ', 'hello ', 'hello ', 'hello ', 'hello ']
print(t1*5)#('world', 'world', 'world', 'world', 'world')

print('-'*10 +'in判断是否存在')
str1='abcd'
list1 =[10,20,30,40]
t1 = (100,200,300,400)
dict1 = {'name':'Python','age':30}

#in 和not in
#1. 字符a是否存在
print('a' in str1)#True
print('a' not in str1)#False

#数据10 是否存在
print(10 in list1)
print(10 not in list1)

#name是否存在
print('name' in dict1)#True
print('name' not in dict1)#False
print('name' in dict1.values())#False


