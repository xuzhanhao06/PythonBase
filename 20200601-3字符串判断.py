'''
    字符串序列. startswith(子串，开始位置下标，结束位置下标)
'''
mystr = "hello world and itcast and itheima and Python"

#1. startswith():判断字符串是否以某个字符串开头
print(mystr.startswith('hello'))    #True
print(mystr.startswith('hel'))      #True
print(mystr.startswith('hels'))     #False

#2. endswith() 判断是否是某个子串结尾
print(mystr.endswith("Python"))#True
print(mystr.endswith("python"))#False

#3. isalpha() :字母组成
print(mystr.isalpha())#False 因为有空格

#4. isdigit() :判断是否都是数字
print(mystr.isdigit())#False
mystr1='12346'
print(mystr1.isdigit())#True

#5. isalnum() :都是数字+字母的组合 ，则返回true
print(mystr1.isalnum())#True
print(mystr.isalnum())#False  因为有空格
str2='abc123'
print(str2.isalnum())#True

#6. isspace(): 都是 空白返回true
print(mystr.isspace())#False
mystr3='    '
print(mystr3.isspace())#True
