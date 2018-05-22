#__Author: Merci
#__Date: 2018-5-17
file = open('data','r+',encoding='utf-8')
file_read = file.read()#读取到的为list
data=eval(file_read)#转换为字典
print(type(data))
print(data)
back_flag = False
exit_flag = False
while not back_flag:
    for key1 in data.keys():
        print(key1)
    current_layout1 = input('>>:')
    if current_layout1 in data.keys():
        for key2 in data[current_layout1]:
            print(key2)#成都
        while not back_flag:
            current_layout2 = input(">>:")
            if current_layout2 in data[current_layout1].keys():
                for key3 in data[current_layout1][current_layout2]:
                        print(key3)#龙泉
                while not back_flag:
                    current_layout3 = input(">>:")
                    if current_layout3 in data[current_layout1][current_layout2].keys():
                        for key4 in data[current_layout1][current_layout2][current_layout3]:
                            print(key4)
                    elif current_layout3 == 'b':
                        back_flag = True
                        break
            elif current_layout2 == 'b':
                back_flag = True
                break
    elif current_layout1 == 'q':
        back_flag = True
        break
file.close()
