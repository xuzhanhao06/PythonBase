print('-list1增加列表数值---------------------')
print('-----------------------while实现-----')
list1=[]
i=0
while i<10:
    list1.append(i)
    i+=1
print(list1)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('------for实现----------------------------')
list2=[]
for i in range(10):
    list2.append(i)
print(list2)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('------列表推导式实现----------------------------')
list3=[i for i in range(10)]
print(list3)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('------列表推导式实现0-10偶数----------------------------')
list4=[i for i in range(0,10,2)]
print(list4)#[0, 2, 4, 6, 8]

list5=[]
for i in range(10):
    if i%2==0:
        list5.append(i)
print(list5)#[0, 2, 4, 6, 8]

list6=[i for i in range(10) if i%2==0]
print(list6)#[0, 2, 4, 6, 8]

print('------多个for实现列表推导式----------------------------')
list7=[]
for i in range(1,3):
    for j in range(3):
        list7.append((i,j))
print(list7)#[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
list8=[(i,j)for i in range(1,3)for j in range(3)]
print(list8)
#[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
#多for的列表推导式等同于for循环嵌套

