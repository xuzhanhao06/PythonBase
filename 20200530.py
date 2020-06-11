
'''
input('提示信息')
'''
PassWord= input('请输入数字：')
print(f"输入数字是：{PassWord}")
print(type(PassWord))#str <class 'str'>
'''转换数据类型'''
print(type(int(PassWord))) #转换成int  <class 'int'>

list1=[10,20,30]
t1=(100,200,300)

print(tuple(list1)) #(10, 20, 30)
print(list(t1))  #[100, 200, 300]

#eval()将数据转换成原本格式
str1='1'
str2='1.1'
str3='(1000,2000,3000)'
str4='[1000,2000,3000]'
print(type(eval(str2))) #<class 'float'>
print(type(eval(str3))) #print(type(eval(str3)))
print(type(eval(str4))) #<class 'list'>
print(type(eval(str1)))#<class 'int'>