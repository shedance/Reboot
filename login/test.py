#__Author: Merci
#__Date: 2018-5-21
with open('admin.txt', 'r', encoding="utf-8") as file:
    data = file.read()
    print(data.split(' '))