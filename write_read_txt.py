#简单登陆锁定实现
import re
import os
n=1
userName="admin"
passWd="admin1234"
find=True
while 1:
    input_userName=input("用户名>>:")
    input_passWd=input("密码>>:")
    if os.path.exists("F:\\MerciGo\\Reports\\user"):
        userName_block=open("F:\\MerciGo\\Reports\\user",'rt',encoding='utf-8')
        txt_content=userName_block.read()
        txt_list=list(txt_content)
        #print(txt_list)
        #print(txt_content)
        #txt_list_comp=re.findall(input_userName,txt_content)
        txt_list_comp=re.split('\n',txt_content)#将txt文本内容按换行符进行分裂成list
        #print('hhhh:',txt_list_comp)
        #print(txt_list_comp)
        #print(type(txt_list_comp))
        for s in txt_list_comp:
            if s==input_userName:
                print("无法登陆，用户名%s处于锁定状态" % input_userName)
                find = False
                break

        #判定用户名是否已经被锁定状态
        """逐行匹配 貌似这个方法在中文英文交替输入的时候会判定失效，方法不可行
        for s in userName_block.readlines():
            userName_judgement=re.fullmatch(input_userName,s)
            print(type(userName_judgement))
            print(s)
            if userName_judgement:
                print("无法登陆，用户名%s处于锁定状态"%input_userName)
                find = False
                break"""
    else:
        open("F:\\MerciGo\\Reports\\user",'w')
    if input_userName == userName and input_passWd == passWd:
        print("欢迎%s登陆xx系统"%userName)
        break
    elif find==False:
        break
    elif n<3:
        print("登陆失败，密码错误，还有%s次机会！"%(3-n))
        n+=1
    else:
        print("密码错误，登陆失败!\n您已经3次登陆失败，用户'%s'已经被锁定." % input_userName)
        file = open("F:\\MerciGo\\Reports\\user",'r+',encoding='utf-8')
        # r+模式写打开文档时 光标会在文件开头，此时先读read(),读取到内存，贯标会移动到内容末尾再进行写入操作则不会覆盖之前的额内容
        file.read()
        file.write("\n%s"%input_userName)#将被锁定的用户名逐行进行写入到txt文档种以便下次输入时判定登陆用户名是否被锁定
        file.close()
        break
