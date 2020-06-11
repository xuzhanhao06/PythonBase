''''
字典不支持下标
如果key存在则修改这个key对应的值;如果key不存在则新增此键值对。
'''''
print('-------------------增加---------------------------')
dict1 = {'name': 'TOM', 'age': 20,'gender':'男'}
#字典序列[key]=值
#id的值是110
dict1['id']=110#新增了id
print(dict1)#{'name': 'TOM', 'age': 20, 'gender': '男', 'id': 110}

dict1['name']='Rose'#修改name
print(dict1)#{'name': 'Rose', 'age': 20, 'gender': '男', 'id': 110}

print('-------------------删除---------------------------')
#删除字典或删除字典中指定键值对。
dict1 = {'name': 'TOM', 'age': 20,'gender':'男'}
# del(dict1)#删除
# print(dict1)#报错！

del dict1['name']#删除name
#del dict1['names']#报错
print(dict1)#{'age': 20, 'gender': '男'}

#clear() 清空字典！
dict1.clear()
print(dict1)   #{}

print('-------------------查找---------------------------')
dict1 = {'name': 'TOM', 'age': 20,'gender':'男'}
#1. [key]
print(dict1['name'])#TOM   返回对应的值（key存在）
#print(dict1['names'])#报错！！！！

print('-------------------函数---------------------------')
dict1 = {'name': 'TOM', 'age': 20,'gender':'男'}
# 2. 函数
#2.1 get()
print(dict1.get('name'))#TOM
print(dict1.get('names'))#None  如果key不存在返回None
print(dict1.get('names','Lissssss'))#Lissssss   如果key不存在返回Lissssss

print('-------------------2.1 keys()查找字典中所有key，返回可迭代对象---------------------------')
print(dict1.keys())#dict_keys(['name', 'age', 'gender'])

print('-------------------value---------------------------')
#查找字典中所有value,返回可迭代对象
print(dict1.values())#dict_values(['TOM', 20, '男'])

print('items（）:'
 '查找字典中所有的键值对，返回可迭代对象，'
  '里面的数据是元组，元组数据1是字典的key,元组数据2是字典key对应的值')
print(dict1)
print(dict1.items())#dict_items([('name', 'TOM'), ('age', 20), ('gender', '男')])


