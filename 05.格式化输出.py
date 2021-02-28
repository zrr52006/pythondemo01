"""

"""

age=18
name='TOM'
weight=75.5
stu_id=1
stu_id1=1000000
# 1.今年我的年龄是X岁  -- 整数 %d
print('今年我的年龄是%d岁' % age )

# 2.今年我的年龄是X岁  -- 字符串 %s、
print('我的名字是%s' % name )

# 3. 我的体重是x公斤 -- 浮点数 %f
print('我的体重是%f公斤' % weight )
print('我的体重是%.3f公斤' % weight )

# 我的学号是X --字符 %s
print('我的学号是%03d' %stu_id) #不足3位的  用0补足
print('我的学号是%03d' %stu_id1) # 超出3位原样输出

# 5.我的名字是X，  -- 整数 %d
print('我的名字是%s，我的年龄是%d岁 ,我的学号是%06d, 我的体重是%.2f' % (name,age,stu_id,weight))