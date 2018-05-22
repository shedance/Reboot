#__Author: Merci
#__Date: 2018-5-21
# -*- coding:utf-8 -*-
import time
def logger(flag = False): # logger（）装饰器函数 ，执行打印log功能，外层再嵌套函数，return spend_time, 而不能再其中再定义函数添加该打印log的功能
    def spend_time(f): #定义的装饰器函数，计算函数运行时间
        def inner(k): #1.inner是一个内部函数  此处如果要装饰的函数为不定长参数用*agrs，**agrs作为形参传入
            start_time = time.time()
            f(k) #2.此处的f为inner函数的外部环境
            end_time = time.time()
            spend_time = end_time - start_time
            print('\nSpend_time:',spend_time)
            if flag == True:
                with open('log.txt','a',encoding='utf-8') as f_log:
                    f_log.write('花费时间:'+str(spend_time)+'\n')
        return inner #返回inner函数名
    return spend_time

def fibo(j): #求Fibonacci数函数
    if j<=2:
        return j-1
    fibo_num = fibo(j-1)+fibo(j-2)
    return  fibo_num

#@spend_time  #装饰器函数 等价于 fibo_list = spend_time(fibo_list)
@logger(flag=True) #装饰器函数@spend_time <=> fibo_list = spend_time(fibo_list) 这种方式规定只能传入一个参数，现在要加另外的一个log打印功能不能就在装饰器函数spend_time上再进行嵌套函数外层logger函数
def fibo_list(m):
    for i in range(1,m+1):
        print (fibo(i),end=' ')
fibo_list(20)  #调用函数计算得到20个斐波那契数列的数需花费的时间
