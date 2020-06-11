def user_info(name,age,gender="男"):
    print(f'您的名字：{name}，年龄{age},性别：{gender}')
print('缺省参数传递')
user_info("Tom",18)#您的名字：Tom，年龄18,性别：男
user_info("Tom",18,"女")#您的名字：Tom，年龄18,性别：女

print('不顺序传递，关键字传递')
user_info(age=35,gender="女",name="Rose")#您的名字：Rose，年龄35,性别：女

print('不定长参数,会返回***元组')
def user_1(*args):
    print(args)

user_1("Tom",18)#('Tom', 18)

print('不定长参数,会返回***集合---组包 过程！')
def user_2(**kwargs):
    print(kwargs)

user_2()
user_2(name="Tom",age=18)#{'name': 'Tom', 'age': 18}


print('************拆包***********************')
print('*拆包1.元组***********************')
def return_num():
    return 100,200

result=return_num()#(100, 200)
num1,num2=return_num()
print(num1,num2)#100 200

print('*拆包2. 字典数据 变量存储是key值***********************')
dict1={'name':'Tom','age':20}
a,b=dict1

#key值
print(a)#name
print(b)#age

#value值
print(dict1[a])#Tom
print(dict1[b])#20




