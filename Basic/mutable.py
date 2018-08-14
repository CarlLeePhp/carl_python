#!/usr/bin/python3

def changeme( a ):
    "修改传入的变量"
    a = 10
    print("函数内的值：", a)
    print("函数内 a 的 id：", id(a))
    return

a = 5
changeme( a )
print("函数外的值：", a)
print("函数外 a 的 id：", id(a))