dict1 = {'name': 'TOM', 'age': 20,'gender':'男'}
print('-----------------key-----------------')
for key in dict1.keys():
    print(key)#name age gender

print('-----------------values-----------------')
for value in dict1.values():
    print(value,end='\t')#TOM	20	男

print('-----------------items-----------------')
for item in dict1.items():
    print(item)
'''''
    ('name', 'TOM')
    ('age', 20)
    ('gender', '男')
'''''
print('-----------------键值对拆包-----------------')
dict1 = {'name': 'TOM', 'age': 20,'gender':'男'}
#items返回的元组数据1是字典的key,元组数据2是字典的value
for key,value in dict1.items():
    print(f'{key}={value}')
    '''''
        ('name', 'TOM')
        ('age', 20)
        ('gender', '男')
    '''''