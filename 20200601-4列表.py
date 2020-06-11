name_list=['TOM','Lily','ROSE']
#1. index()
print(name_list.index('Lily'))#1
#print(name_list.index('Lily222'))#报错

#2.count 个数
print(name_list.count('Lily'))#1
print(name_list.count('Lilssy'))#0

#3. len  长度
print(len(name_list))#3

#1. in 判断是否在里面
print('TOM' in name_list)#True
print('TOMs' in name_list)#False

#2. not in  在的话返回False
print('TOM' not in name_list)#False

#案例：邮箱注册
#name=input('请输入您的邮箱账户名')
name='TOM'
if name in name_list:
    #提示用户已注册
    print(f'您输入的名字是{name},此用户名已经存在')
else:
    print(f'您输入的名字是{name},可以注册')