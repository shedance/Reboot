#-*-coding:utf-8-*-

print("37.题目：对10个数进行排序。")
#digital_list=[]
#s=[1,3,4,5,8,8,0,7,5,2]
s=[]
for m in range(0,10):
    s.append(int(input("输入第%s个数："%(m+1))))
for i in range(0,9):
    for j in range(0,9):
        if s[j]<s[j+1]:
            tmp = s[j+1]
            s[j+1]=s[j]
            s[j]=tmp
print("降序排列结果：",s)

