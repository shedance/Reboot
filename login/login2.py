#__Author: Merci
#__Date: 2018-5-22
#启动页面start()
def start():
    page_list = ['Home','Finance','Book']
    for i,item in enumerate(page_list):
        print(i+1,item)
    return len(page_list)

#从txt种获取已经存好的账号和密码{'userName':'admin','passWd':'1234'}
def authentic(auth):
    if auth =='jd':
        print("Please use the JingDong Accout to loggin！")
        with open ('jd.txt','r',encoding='utf-8') as file_data:
            data = eval(file_data.read())
            user_name = input('JingDong_Account>>:')
            pass_word = input('Password>>:')
            if data['userName'] == user_name and data['passWd'] == pass_word:
                return True
            else:
                return False
    else:
        print("Please use the WeiXin Accout to loggin！")
        with open('wx.txt', 'r', encoding='utf-8') as file_data:
            data = eval(file_data.read())
            user_name = input('WeiXin_Account>>:')
            pass_word = input('Password>>:')
            if data['userName'] == user_name and data['passWd'] == pass_word:
                return True
            else:
                return False
#新增登陆功能装饰器方式
login_status_jd = False #默认为未登陆状态 两种登陆方式，需要用两个状态分别判断各自是否登陆，不能存在一个变量中。
login_status_wx = False
def login_check(auth):
    def login_f(f):#传入需要使用装饰器添加该登陆功能的函数名
        def login_inner():
            global login_status_jd #函数内需要更改全局变量
            global login_status_wx
            if auth == 'jd': #京东账户登陆
                if not login_status_jd:
                    if authentic(auth):
                        print('JingDong Accout login sucessfully!')
                        f() #需要使用装饰器添加功能的函数
                        login_status_jd = True #修改全局变量值
                    else:
                        print('Accout or Password is wrong!')
                else:
                    print('JingDong Account has login.')
                    f()
            else: # 微信登陆
                if not login_status_wx:
                    if authentic(auth):
                        print('WeiXin Accout login sucessfully!')
                        f()
                        login_status_wx = True
                    else:
                        print('Accout or Password is wrong!')
                else:
                    print('WeiXin Account has login.')
                    f()
        return login_inner
    return login_f

@login_check('jd')
def home():
    print('Welcome to JingDong Home page!')

@login_check('wx')
def finance():
    print('Welcome to JingDong Finance page!')

@login_check('jd')
def book():
    print('Welcome to JingDong Book page!')

#功能执行
while True:
    list_num = start()
    page_id = input ("Select the Page ID>>:").strip()
    if len(page_id)==0:continue
    if page_id.isdigit():
        page_id = int(page_id)
        if page_id ==1:
            home()
        elif page_id == 2:
            finance()
        elif page_id == 3:
            book()
        else:
            print("Page ID doesn't exist！")
    elif page_id == 'q':
        print("Exit...")
        break
    else:
        print("The inputting is wrong, Please try again!")







