#__Author: Merci
#__Date: 2018-5-21

#当前目录存放jd_admin.txt 和 wx_admin.txt 分别写入两种账户的名称和密码，为了方便账号和密码用空格分开，仅一组数据以便读取

#启动页面展示page选项Home，Finace，Book
def start():
    start_list = ['Home','Finance','Book']
    for i,item in enumerate(start_list):
        print(i+1,".",item)

#登陆方式验证，读取存储的正确账号密码，返回结果以list的方式
def authentic(auth = 'jd'):
    if auth == 'jd':
        with open('jd_admin.txt','r',encoding='utf-8') as file:
            data = file.read()
            userdata_list=data.split(' ')
            return userdata_list
    else:
        with open ('wx_admin.txt','r',encoding='utf-8') as file:
            data = file.read()
            userdata_list = data.split(' ')
            return userdata_list
#登陆状态默认为False
login_status1 = False # 京东账户登陆状态
login_status2 = False #微信账户登陆状态
#装饰器函数，登陆检测和登陆执行
def login_check(login_status):
    def login(f):
        def login_inner(auth):
            if auth == 'jd':
                global login_status1
                if not login_status1:
                    print("您还没有登陆，请输入京东账户和密码进行登陆！")
                    userdata=authentic(auth)
                    userName = userdata[0]
                    passWd = userdata[1]
                    user= input("京东账户名>>:")
                    password = input("密码>>:")
                    if user == userName and password == passWd:
                        print("登陆成功!")
                        f(auth)
                        login_status1= True
                    else:
                        print("用户名或者密码错误")
                else:
                    f(auth)
            else:
                global login_status2
                if not login_status2:
                    print("该页面需要使用您的微信账户登陆，请输入微信账户和密码进行登陆！")
                    userdata = authentic(auth)
                    userName = userdata[0]
                    passWd = userdata[1]
                    user = input("微信号>>:")
                    password = input("密码>>:")
                    if user == userName and password == passWd:
                        print('登陆成功！')
                        f(auth)
                        login_status2 = True
                    else:
                        print("用户名或者密码错误！")
                else:
                    f(auth)
        return login_inner
    return login


@login_check(login_status1)
def Home(auth = 'jd'): # 京东账号登陆 auth = 'jd'
    print('Welcome to JingDong Home Page')

@login_check(login_status2)
def Finance(auth = 'wx'): #微信账号登陆 auth = 'wx'
    print('Welcome to Jingdong Finance Page')

@login_check(login_status1)
def Book(auth='jd'): #京东账号登陆  auth='jd'
    print('Welcome to JingDong Book Page')

#执行功能
while True:
    start() #显示首页
    print("** q退出程序！**")
    page_id = input("Select the Page_ID>>:").strip()
    if page_id == 0: continue
    elif page_id.isdigit():
        page_id = int(page_id)
        if page_id == 1:
            Home(auth='jd')
            continue
        elif page_id == 2:
            Finance(auth='wx')
            continue
        elif page_id == 3:
            Book(auth='jd')
            continue
        else:
            print("输入页面ID不存在！请重新选择！")
    elif page_id == 'q':
        print('退出程序。。。')
        break
    else:
        print("输入错误！请重新输入！")
