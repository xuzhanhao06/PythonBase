mystr="hello world and itcast and itheima and Python"

'''
replace() 把and 换成he
,有返回值,没有改原数据
'''
# new_str=mystr.replace('and','he')
# print(mystr)
# print(new_str)

new_str=mystr.replace('and','he',1)
print(mystr)
print(new_str)

#2. split() 分割，返回一个列表
#会丢失分割字符
list1=mystr.split('and')#['hello world ', ' itcast ', ' itheima ', ' Python']
list1=mystr.split('and',2)#['hello world ', ' itcast ', ' itheima and Python']
print(list1)

#3. join() --合并列表里面的字符串数据为一个大字符串
mylist=['aa','bb','ccc']
new_str='...--'.join(mylist)
print(new_str)#aa...--bb...--ccc

#4. caplitalize() :将字符串第一个字符转换成大写
print(mystr. capitalize())#Hello world and itcast and itheima and python

#5. title() 每个单词首字母都转换成大写
print(mystr.title())#Hello World And Itcast And Itheima And Python

#6. upper() 小写转大写
new_str=mystr.upper()
print(mystr.upper())#HELLO WORLD AND ITCAST AND ITHEIMA AND PYTHON

#7. lower #大写转小写
print(new_str.lower())# hello world and itcast and itheima and python
print('----------------------------------------------------------')
mystr="  hello world and itcast and itheima and Python  "
print(mystr)
#1. lstrip()
print(mystr.lstrip()) #删除左侧空白字符
#2. rstrip() #删除右侧空白字符
print(mystr.rstrip())
#strip() #删除两侧空白字符
print(mystr.strip())

#ljust()左对齐
#rjust 右对齐
#center居中对齐
mystr1='hello'
print(mystr1.ljust(10,'.'))#hello.....
print(mystr1.rjust(10,'.'))#.....hello
print(mystr1.center(10,'.'))#..hello...