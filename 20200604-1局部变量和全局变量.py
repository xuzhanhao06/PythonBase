a=100

def testA():
    a=111
    print(a)

def testB():
    print(a)

def testC():
    # 关键字声明a为全局变量
    global a
    a=200
    print(a)

testA()#111
testB()#100
testC()#200
testB()#200
