#将8人分配3教室

'''
1. 准备数据
2.分配
3.验证
'''
import  random
#1.
teachers=['A','B','C','D','E','F','G','H']
offices=[[],[],[]]
#2.
for name in teachers:
    #列表追加数据--append extend insert
    num=random.randint(0,2)
    offices[num].append(name)
print(offices)
#3.
#办公室+个编号
i=1
for office in offices:
    #打印人数
    print(f'办公室{i}人数：{len(office)},老师分别是：',end="")
    #打印名字
    for name in office:
        print(name,end=' ')
    print()
    i+=1