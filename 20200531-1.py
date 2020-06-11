import random

#玩家
#player=int(input("请出拳：0--石头 1---剪刀  2--布"))
player=1
#电脑 取随机数
computer=random.randint(0,2)

#判断输赢
if ((player==0) and (computer==1))or((player==1) and (computer==2))or((player==2) and (computer==0)):
    print("你赢了~")
elif player==computer:
    print("平局")
else:
    print("电脑获胜")
print("---------------------------------------------")
#三元运算符
a=1
b=2
c = a if a>b else b
#(条件满足时执行)if(先判断条件) else(否则执行这)
print(c)
print("---------------------------------------------")
i=1
while i<=5:
    print(f"第{i}")
    i+=1
print("---------------------------------------------")

n=1
result=0
while n<=100:
 #   result +=n
 if(n%2==0):
    result += n
 n +=1
print(result)

print("---------------------------------------------")
#输出 倒三角
j=0
while j<=4:
    i=j
    while i<=4:
        print('*',end='')
        i+=1
    print()
    j+=1

print("---------------------------------------------")
#正三角
j=0
while j<=4:
    i=0
    while i<=j:
        print('*',end='')
        i+=1
    print()
    j+=1
print("---------------九九乘法表----------------------------------")
j=1
while j<=9:
    #一行的表达式
    i=1
    while i<=j:
        print(f'{i}*{j}= {i*j}',end='\t')
        i+=1
    print()
    j+=1

