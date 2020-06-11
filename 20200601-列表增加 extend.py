name_list=['TOM','Lily','ROSE']
#extend():列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
name_list.extend('xiaoming')

#['TOM', 'Lily', 'ROSE', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g']
print(name_list)

name_list.extend(['xiaoming','xiaohong'])
#['TOM', 'Lily', 'ROSE', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g', 'xiaoming', 'xiaohong']
print(name_list)

#extend 追加数据是一个序列，需拆开逐一加待结尾