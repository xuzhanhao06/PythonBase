print('集合中的数据不能重复,不支持下标,没有数据')
print('1.创建有数据的集合')
s1={10,20,30,40,50}
print(s1)#{40, 10, 50, 20, 30}
s2={10,20,30,40,50,50}
print(s2)#{40, 10, 50, 20, 30}

s3=set('abcdefg')
print(s3)#{'g', 'd', 'b', 'f', 'a', 'e', 'c'}
print('-----2.创建空数据的集合------------')
s4=set()
print(s4)#set()

print(type(s4))#<class 'set'>
s5={}
print(type(s5))#<class 'dict'>
print('总结：创建集合使用{}或set()，但是如果要创建空集合只能使用set()，因为{}用来创建空字典。')
