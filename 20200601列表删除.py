name_list=['TOM','Lily','ROSE']
#1. del
#del name_list
#del(name_list)
print(name_list)#已经删除 会报错

#del 可以删指定下标数据
del name_list[0] #['Lily', 'ROSE']
print(name_list)

name_list=['TOM','Lily','ROSE']
#pop() --删除指定下标数据 ，默认删最后一个 ，返回删除数据
del_name=name_list.pop()
print(del_name)#ROSE
print(name_list)#['TOM', 'Lily']

name_list=['TOM','Lily','ROSE']
del_name=name_list.pop(1)
print(del_name)#Lily
print(name_list)#['TOM', 'ROSE']


#3. remove(数据)--删除匹配的第一个数据
name_list=['TOM','Lily','ROSE']
name_list.remove('ROSE')
print(name_list) #['TOM', 'Lily']

#4. clear()  --清空
name_list=['TOM','Lily','ROSE']
name_list.clear()
print(name_list)#[]