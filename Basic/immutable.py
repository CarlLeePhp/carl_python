#!/usr/bin/python3

def changeme( mylist ):
    "修改传入的列表"
    mylist.append(5)
    print("修改后函数内取值：", mylist)
    return

def changeyou( mylist ):
    "赋值？还是定义了一个局部变量？"
    mylist = [10, 20, 30, 40]
    print("赋值后函数内取值：", mylist)
    return

mylist = [1, 2, 3, 4]
changeme( mylist )
print("修改后函数外取值：", mylist)
changeyou(mylist)
print("赋值后函数外取值：", mylist)