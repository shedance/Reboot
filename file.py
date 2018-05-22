#__Author: Merci
#__Date: 2018-5-17
file = open('f1.txt','r+',encoding='utf-8') #
file2 = open('f2.txt','w+',encoding='utf-8')
num=0
for line in file:
    num += 1
    if num == 6:
        line=''.join([line.strip(),'GOGOFighting\n'])
    file2.write(line)
file.close()
file2.close()