mystr="hello world and itcast and itheima and Python"
#1. find()
print(mystr.find('and')) #12
#15下标开始到30下标结束
print(mystr.find('and',15,30)) #23

#不存在返回 -1
print(mystr.find('ands')) #-1

#2. index（）
print(mystr.index('and'))#12
#print(mystr.index('ands'))# index 不存在会报错

#3. count（）
print(mystr.count('and',15,30))#1  表示and出现1次
print(mystr.count('and'))#3   表示and出现了三次
print(mystr.count('ands'))#0

#4. rfind()  从右侧开始查找
print(mystr.rfind('and'))#35

#5. rindex()
print(mystr.rindex('and'))#35
#print(mystr.rindex('ands'))#报错
