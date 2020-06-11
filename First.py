'''
这是多行注释
'''
Num=15
Str="Tom"
Flot=1.1
stu_id=1
print("Hello World 1")
print("Hello World 2")
print("有%d数字" %Num)
print("有%s字符" %Str)
print("有%f字符" %Flot)#有1.100000字符
print("有%.2f字符" %Flot) #保留2位小数 有1.10字符
print(type(Num))  #type数据类型

'''
我的学号是001  
3：3位  ，0：用0补全
'''
print("我的学号是%03d"%stu_id)

'''
两个变量输出
'''
print("我的学号：%06d,名字：%s" %(stu_id,Str) )#我的学号：000001,名字：Tom
#可以都用%s
print("我的学号：%06s,名字：%s" %(stu_id,Str) )#我的学号：     1,名字：Tom

'''
f --格式化字符串
'''
print(f"我的学号：{stu_id},名字：{Str}")#我的学号：1,名字：Tom

''''  \n --换行 \t --4个空格   '''
print("\tHello \n\tWorld")

'''结束符 end  '''
print("Hello",end='\t')
print("Hello",end='\n')
print("Hello",end='。。。')











'''
这是个注释啊
'''

'''
你说呢
'''