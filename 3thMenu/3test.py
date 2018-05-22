#__Author: Merci
#__Date: 2018-5-18
#初始化 将menu存入磁盘中

# menu = {'北京':{
#     '朝阳':{
#         '国贸':{
#             'CICC':{},
#             'HP':{},
#             '渣打银行':{},
#             'CCTV':{}
#         },
#         '望京':{
#             '陌陌':{},
#             '奔驰':{},
#             '360':{}
#         },
#         '三里屯':{
#             '优衣库':{},
#             'apple':{}
#         }
#     },
#     '昌平':{
#         '沙河':{
#             '老男孩':{},
#             '阿泰包子':{}
#         },
#         '天通苑':{
#             '链家':{},
#             '我爱我家':{}
#         },
#         '回龙观':{}
#     },
#     '海淀':{
#         '五道口':{
#             '谷歌':{},
#             '网易':{},
#             'Souhu':{},
#             'Sogo':{},
#             '快手':{}
#         },
#         '中关村':{
#             'youku':{},
#             'Iqiyi':{},
#             '汽车之家':{},
#             '新东方':{}
#         }
#     }
# },
#         '上海':{
#             '浦东':{
#                 '陆家嘴':{
#                     'CICC':{},
#                     '高盛':{},
#                     '摩根':{}
#                 },
#                 '外滩':{}
#             },
#             '闵行':{},
#             '静安':{}
#         },
#         '山东':{
#             '济南':{},
#             '德州':{
#                 '乐陵':{
#                     '丁务镇':{},
#                     '城区':{}
#                 },
#                 '平原':{}
#             },
#             '青岛':{}
#         }
# }

# a=str(menu)
# with open('menu','w',encoding='utf8') as f:
#     f.write(a)
#读取menu
with open('menu','r',encoding='utf8') as f:
    menu = eval(f.read().strip())
parent_layers=[]
current_layer = menu
while True:
    print('欢迎使用省市查询系统'.center(50,'*'))
    for key in current_layer:
        print('>>>',key)
    print('输入你要查询的地区省市或新增[add]、修改[revise]、删除[delete]、返回上一级[q]')
    choice = input('>>>').strip()
    #查询
    if choice in current_layer:
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    #新增
    elif choice == 'add':
        user_add = input('请输入你要添加的省市区:').strip()
        if user_add in current_layer:
            print('此项已存在，请重新输入')
        else:
            current_layer[user_add]={}
            continue
    #修改
    elif choice =='revise':
        user_revise = input('请输入要修改的省市区:').strip()
        if user_revise in current_layer:
            user_revise_after = input('修改为:').strip()
            current_layer[user_revise_after]=current_layer[user_revise]
            del current_layer[user_revise]
            continue
    #删除
    elif choice =='delete':
        user_delete = input('请你输入要删除的省市区:').strip()
        if user_delete in current_layer:
            parent_layers.append(current_layer)
            del current_layer[user_delete]
            continue
        else:
            print('此项不存在，请重新输入:')
    #返回上一级或退出
    elif choice == 'q':
        if parent_layers:
            current_layer = parent_layers.pop()
        else:
            print('目前为最上级菜单，输入q后为退出系统！')
            break
    else:
        print('输入非法，请重新输入选择！')
if type(current_layer) != list:
    with open('menu','w',encoding='utf8') as f:
        f.write(str(current_layer))