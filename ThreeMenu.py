#__Author: Merci
#__Date: 2018-5-14
provence_city_conutry ={
    '四川':
        {'成都':
             ['锦江区','武侯区','高新区','成华区','青羊区','金牛区'],
         '达州':
             ['大竹','渠县','达县','开江','宣汉']},
    '重庆':
        {'重庆市':
             ['江北','渝北','朝天门','沙坪坝','观音桥']},
    '北京':
        {'北京市':
             ['海淀区','天安门','东直门','中关村']}}
provence_list=[]
exit_flag=False
print("====ID====省名====")
for i, j in enumerate(provence_city_conutry.keys()):
    print("----%d----%s----" % (i + 1, j))
    provence_list.append(j)
while 1:
    if exit_flag==True:
        print("退出程序....")
        break
    provence_ID = input("\n输入省名ID('Q'退出程序)>>:")
    if provence_ID.isalpha():
        if provence_ID =='Q':
            print("退出程序....")
            break
        else:
            print('1-3##重新输入正确ID！')
            continue
    elif provence_ID.isdigit():
        provence_ID=int(provence_ID)
        if provence_ID>0 and provence_ID<=len(provence_list):
            provence=provence_list[provence_ID-1]
            #打印该省对应的市区
            print("====ID====市====")
            city_list = []
            for k,l in enumerate(provence_city_conutry[provence].keys()):
                print("----%d----%s----"%(k+1,l))
                city_list.append(l)
            while 1:
                city_ID = input("\n输入城市的ID('#'返回上层,'Q'退出程序)>>:")
                if city_ID=='#':
                    break
                elif city_ID.isalpha():
                    if city_ID == 'Q':
                        exit_flag=True
                        break
                    else:
                        print("2-3##输入有误，重新输入！")
                        continue
                elif city_ID.isdigit():
                    city_ID=int(city_ID)
                    if city_ID>0 and city_ID<=len(city_list):
                        city=city_list[city_ID-1]
                        #显示县城
                        print("====ID====县名====")
                        for m,n in enumerate(provence_city_conutry[provence][city]):
                            print("----%d----%s----"%(m+1,n))
                    else:
                        print("2-1##输入市ID有误，请重新输入！")
                else:
                    print("2-2##输入市ID有误，请重新输入！")
                    continue
        else:
            print("1-1##输入省ID有误，重新输入！")
    else:
        print("1-2##输入省ID有误，请重新输入！")
        continue


