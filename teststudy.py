# #__Author: Merci
# #__Date: 2018-5-20
# count = 10
# def outer():
#     global count
#     print(count)
#     count = 5
#     print("count2:",count)
# outer()
# print ("count3:",count)
#
# s = set([1,2,3])
# s2= set([1,2])
# print(s ^s2)
# print(s)

# def f(n): #函数f()
#     return n**2
#
# def f2(a,b,function): #函数f2（）
#     return f(a)+f(b)
#
# s = f2(2,3,f) #将函数f作为一个参数传给f2
# print(s)

# def func():
#     def inner():
#         x = 7
#         return x
#     return inner  #返回一个函数名字
#
# a = func()
# print('a的类型:%s'%type(a))
# print('a的值：%s'%a) #a此时指向inner函数内存空间地址
# print(a())  #a()就相当于直接调用func函数中的inner（）函数效果

# def f(n):
#     if n == 1: #递归函数需要有一个结束条件，求阶乘时当n=1时就结束了
#         return 1
#     else:
#         sum = n* f(n-1)
#         return sum
# print(f(5)) # 5！=120

# 函数调用过程实现阶乘
# 5*f(4)
#     4*f(3)
#         3*f(2)
#             2*f(1)
#                 1
#斐波那契数列： 0，1，1，2，3，5，8，13，21，34,55...
# def f(n):  #定义函数求得斐波那契数列第n个数的是多少：
#     if n ==1:
#         return 0
#     if n == 2:
#         return 1
#     fibo_n =f(n-2)+f(n-1)
#     return fibo_n
#
# n= int(input(">>:")) #循环输出斐波那契数列
# for i in range(1,n+1):
#     print(f(i),end='\t')
#
#
# def fibo_list(n):
#     if n<=2:
#         return n-1
#     fibo_n=f(n-1)+f(n-2)
#     return fibo_n
# print('\n',fibo_list(8))
#
# def f3(s): # 定义需要过滤掉得内容函数
#     if s!= 'a':
#         return s
# s1 = ['x','y','z','u','v','w']
# s2 = filter(f3,s1) #filter（）方法中传入函数f3
# print("通过f3函数过滤掉得到s2内存空间地址:>",s2)
# print(list(s2))  #使用list方法进行强转为list
# def f4(s):
#     return s+ "admin"
#
# s1 = ['x','y','z','u','v','w']
# s3 = map(f4,s1)
# print(s3)
# print(list(s3))
# from functools import reduce
# def add(x,y):
#     return x+y
# sum = reduce(add,range(1,101))
# print(sum) #reduce的结果就是一个值
#
# from functools import reduce
# def factorial(x,y):
#     return x*y
# factorial_num = reduce(factorial,range(1,6)) #reduce()方法求5！结果
# print(factorial_num)
#
# from functools import reduce
# factorial = lambda x,y:x*y
# factorial_num = reduce(factorial,range(1,6))
# print(factorial_num)
# #合成一句代码
# factorial_num2 = reduce(lambda x,y:x*y,range(1,6)) #5!值
# print(factorial_num2)
# y=8
# def outer():
#     x=10
#     def inner():
#         print(y)
#     return inner
# f = outer()
# f()
import time
def spend_time(f): #定义的装饰器函数，计算函数运行时间
    def inner(k): #1.inner是一个内部函数  此处如果要装饰的函数为不定长参数用*agrs，**agrs作为形参传入
        start_time = time.time()
        f(k) #2.此处的f为inner函数的外部环境
        end_time = time.time()
        spend_time = end_time - start_time
        print('\nSpend_time:',spend_time)
    return inner #返回inner函数名

def fibo(j): #求Fibonacci数函数
    if j<=2:
        return j-1
    fibo_num = fibo(j-1)+fibo(j-2)
    return  fibo_num

@spend_time  #装饰器函数 等价于 fibo_list = spend_time(fibo_list)
def fibo_list(m):
    for i in range(1,m+1):
        print (fibo(i),end=' ')
fibo_list(35)  #调用函数计算得到20个斐波那契数列的数需花费的时间

# fibo_list = spend_time(fibo_list)
# fibo_list(20)


# def outer():
#     a=10
#     def inner(): #inner是一个内部函数
#         print(a) #调用外部环境的变量，但是不是全局作用域的
#
#     return inner #inner就是一个闭包函数