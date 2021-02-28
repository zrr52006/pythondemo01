"""
1. 按照经验将不同的变量存储不同类型的数据
2.验证这些数据到底是什么类型--检测数据类型 -- type(数据)
"""
# int 整型
num1=1
# float 浮点型  就是小数
num2=1.1
print(type(num1))
print(type(num2))

# str 字符串  特点：数据都要带引号
a='hello world'
print(type(a))

# bool bool--布尔类型，通常判断使用
b=True # False
print(type(b))



# list 列表
c =[10,20,30]
print(type(c))

# tuple 元组
d=(10,20,30)
print(type(d))

# set 集合
e={10,20,30}
print(type(e))

# dict 字典  键值对
f={'name':'zrr','age':18}
print(type(f))
'''
list 列表
tuple 元组
set 集合
dict 字典
'''
