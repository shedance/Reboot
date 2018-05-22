#__Author: Merci
#__Date: 2018-5-17
f = open('data2','r+',encoding="utf-8")
data = f.read()
print(type(data))
print(eval(data))
x= str(eval(data))
print (x)
print('11',x.split(','))


d1=dict.fromkeys(['host1','host2','host3'],'Mac')
print(d1)


d2=dict.fromkeys(['host1','host2','host3'],['Mac','huawei'])
print(d2)