print("---------------for循环----------------------------------")
#for 临时变量 in 序列

str1='ssisesi'
for i in str1: #打印字符串
    # if i=='e' :
        #break
    #    continue
    print(i,end='\t')

print()
print("---------------while 以及 else----------------------------------")
i=0
while i<=5:
    print(f"{i}",end='\t')

    i+=1
else: #正常结束后就会执行  #break 非正常执行 不会执行else
    print("呸呸 正常结束后就会执行  #break--非正常执行,不会执行else")
    print("#continue 是正常的")

print("---------------for 以及 else----------------------------------")

str1='ssadasdafff'
for i in str1:
    print(f'{i}',end='\t')
else:#正常结束后就会执行  一定会被执行一次
    print("执行拉！正常结束后就会执行 #break--非正常执行,不会执行else")
    print("#continue 是正常的")
print("---------------'' 和 " " 和''' '''----------------------------------")

str2='''i am 
Tom'''
print("str2",str2)

str3="zxcvbnm"
print(str3[0])#下标精确找
print(str3[3])#下标精确找
print("---------------切片----------------------------------")
#序列名[开始下标：结束下标：步长]
str4="0123456789"
print(str4[2:5:2]) #24
print(str4[2:5]) #234 步长默认为1
print(str4[:5]) #01234 默认从0开始
print(str4[:])#0123456789 选取所有
print(str4[::-1])#9876543210 步长为负数 ，表示倒叙选取
print(str4[-4:-1])#678
''' 如果选取方向与步长方向冲突，则无法选取数据'''
print(str4[-4:-1:-1])# 无 ！输出！！！！！！！
print(str4[-1:-4:-1])#987