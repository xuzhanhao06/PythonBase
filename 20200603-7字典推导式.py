#创建字典key是1-5的数字， v是这个数字的平方
dict1={i:i**2 for i in range(1,5)}
print(dict1)#{1: 1, 2: 4, 3: 9, 4: 16}

print('******************将两个列表合并为一个字典**************************')
list1 =['name','age','gender']
list2 = ['Tom', '20','man']
dict1={list1[i]:list2[i] for i in range(len(list1))}
print(dict1)#{'name': 'Tom', 'age': '20', 'gender': 'man'}
'''''
1.如果两个列表数据个数相同，len统计任何一个列表的长度都可以
2.如果两个列表数据个数不同，len统计数据多的列表数据个数会报错:len统计数据少的列表数据个数不会报错
'''''

print('******************提取字典中目标个数**************************')
counts={'MBP':268,'HP':125,'DELL':201,'Lenovo ':199,'acer':99}
#1. 需求：提取台数大于等于200
#获取所有数据
print(counts.items())#dict_items([('MBP', 268), ('HP', 125), ('DELL', 201), ('Lenovo ', 199), ('acer', 99)])
dict1={key:value for key,value in counts.items() if value>=200}
print(dict1)












