name_list=['TOM','Lily','ROSE']

#1. 修改指定下标的数据
name_list[0]='aaa'
print(name_list) #['aaa', 'Lily', 'ROSE']

#2. 逆序 reverse()
list1=[1,3,5,2,6,8]
list1.reverse()
print(list1)#[8, 6, 2, 5, 3, 1]

#3.sort() 排序：升序(默认)与 降序,可以设置 key=‘。。。’关键字排序
list1=[1,3,5,2,6,8]
list1.sort()  #[1, 2, 3, 5, 6, 8]
print(list1)

list1.sort(reverse=True)  #[8, 6, 5, 3, 2, 1]
print(list1)


