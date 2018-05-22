#__Author: Merci
#__Date: 2018-5-17
#读取目录中的已有数据，with方法自行file.close(),则不手动调用该方法关闭文件
# file = open('data','r',encoding='utf-8')
# file_read = file.read()#读取到的为list
#data=eval(file_read)#转换为字典
with open('data2','r',encoding = 'utf-8') as file:
    file_read=file.read()
    data = eval(file_read)
exit_flag = False
current_layout = data
last_layout_dic = data
global_data = data
last_layout = []
num = 0
print("help:----------------------------\n\te->Add item to the current list \n\tb->Back to last list \n\td->Delete item in the current list \n\t------------------------".center(20))
while not exit_flag:
    print("======Area_List=====")
    for key in current_layout:
            print (key.center(13))
    print("====================")
    choices = input ("Input the Area Name>>:").strip()
    if len(choices)==0:
        continue
    elif choices in current_layout:
        num += 1
        choices2 = choices
        last_layout.append(current_layout)
        last_layout_dic = current_layout
        current_layout = current_layout[choices]
    elif choices == 'e':
        add_items = input("input Add items>>:").strip()
        if len(add_items) == 0:
            continue
        current_layout[add_items] = {}
        continue
    elif choices == 'd':
        input_del_item = input("Input the item you want to delete>>:").strip()
        if input_del_item == 0:
            continue
        elif input_del_item in current_layout:
            del_item = current_layout.pop(input_del_item)
            print("Delete %s sucessfully"%input_del_item )
        else:
            print("The inputting is right?? or the item doesn't exist!")
            continue
    elif choices == 'c':
        input_change_item = input("Input the item you want to change>>:").strip()
        if input_change_item == 0: continue
        elif input_change_item in current_layout:
            #current_layout.pop(input_change_item) #要修改菜单目录中的其中一项，先删除该键值对
            changed_item = input("Input the new item>>:").strip()
            if changed_item == 0: continue
            elif changed_item in current_layout:
                print("%s 已经存在于目录中，请检查输入是否有误！"%changed_item)
            else:
                current_layout[changed_item] = current_layout[input_change_item]
                current_layout.pop(input_change_item)
                print('The %s has been changed:%s'%(input_change_item,changed_item))
        else:
            print("The item doesn't exist you want to change")

    elif choices == 'b':
        if len(last_layout)==0:
            print('不能返回，已经是第一层，退出程序。。')
            break
        else:
            current_layout = last_layout.pop()
            print(current_layout)
    #在添加地名区域的过程中只能是逐一返回到上一层直至退出才能逐一获取到添加或者删除的项目，所以此处不不用退出项目，在第一层返回时直接退出。
    #last_layout.pop()，返回时执行回到上一层，如果当前层中有添加或者删除时更新到返回上层目录字典。
    # elif choices == 'q':
    #     exit_flag = True
    #     print('退出程序。。')
    else:
        print ('请按目录提示输入')
#print(current_layout)
if type(current_layout) != list:
    with open('data2','w',encoding='utf-8') as file_update:
        file_update.write(str(current_layout))


