#如果想要存储多个数据，但是这些数据是 不能修改的数据 ,----元组
#元组特点:定义元组使用小括号，且逗号隔开各个数据，数据可以是不同的数据类型。
t1=(10,20,30)
print(t1)#(10, 20, 30)
print(type(t1))#<class 'tuple'>

t2=(10,)
t3=(10)

print(type(t2))#'tuple'
print(type(t3))# 'int'
t4=('aaa')
print(type(t4))# 'str'
t5=('aaa',)
print(type(t5))#tuple
