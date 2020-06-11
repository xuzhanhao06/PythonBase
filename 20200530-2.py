Num1=2**4  #次方 16
Num=9//4  #2  整除
Num **=4  #Num=Num ** 4
print(Num) #16


Num1,Str1,Float1=15,"Tom",75.2   #多变量赋值

Num1 +=1 +1  #17

print(Num1)
print(not (Num1<Num and Num<Num))

print("---------------------------------------")
#age=int(input("请输入年龄："))
age=18
if age<18:
    print("给我滚~下车 这不去幼儿园！")
    print("条件执行3")
elif age>=60:
    print(f" age={age},太老啦！会不懂的！")
elif 18<=age<=60:
    print("可以开车！嘀嘀嘀~")
    print("条件执行1")
    print(f" age={age}")
else:
    print("错误！")
print("---------------------------------------")
money=1
seat=1
if money==1:
    print("土豪！上车")
    #判断是否能坐
    if seat==1:
        print("有座位，坐下了~")
    else:
        print("土豪！给我站着！")

else:
    print("没钱没钱~")