#-*- coding:utf-8 -*-
#print("购物车程序，要求用户先输入存款，\n然后打出商品列表，用户输入商品编号进行购买，\n如果存款不足就提示用户余额不足，差多少钱，\n如果存款足够就将商品加入购物车，并显示余额，\n用户可以连续购物，\n直到用户选择退出后，才终止购物，并打印出已购买的商品列表（包括每件商品的价格）")
print("=====================没有假货的淘宝商店=======================\n".center(100))
print('开业大吉，郑重申明\n'.center(100))
print("==========本购物程序仅对土豪们开放，如不是土豪请绕道==============".center(100))
cunkuan=int(input('请亮出您的钱包(单位万元)：'))
shangping = {'豆浆':500,'油条':200,'包子':1000,'肉饼':300,'牙刷':200,'台灯':1000,'iPhone':1000000}
gouwuche={}
print("\n商品列表\n---商品编码ID---------名称---------价格(单位:万元)---")
i=0
jiage=[]
name=[]
#列出商品清单
for key,values in shangping.items():
    i+=1
    print("------[%s]------------ %s-------------%s------"%(i,key,values))
    jiage.append(values)
    name.append(key)
all_sccess=0
all_fail=0
gouwuche_name=[]
gouwuche_jiage=[]
gouwuche_jiage_fail=[]
gouwuche_name_fail=[]
m_id=[]
s=0
while 1:
    m=input("输入购买商品ID>>:")
    if m=='quit':
        break
    else:
        m=int(m)
        m_id.append(m)
        i=m-1
        if i>=len(name):
            print("**商品ID不存在")
        else:
            all_sccess = all_sccess + jiage[i]
            all_fail=all_fail+jiage[i]
            #print("---------总价:", all_fail)
            if  all_fail>cunkuan:
                all_fail = all_fail - jiage[i]
                if name[i] in gouwuche_name_fail:
                    #all_fail=all_fail-jiage[i]
                    #print("总价2:",all_fail)
                    #print("名称",name[i])
                    #print("购物车的已选中的总价",sum(gouwuche_jiage))
                    l=gouwuche_name_fail.index(name[i])
                    #print("购物车的价格L",gouwuche)
                    #print("失败",gouwuche_jiage_fail[l])
                    if s==1:
                        print("**%s:%s元，加入购物车失败" % (gouwuche_name_fail[l], gouwuche_jiage_fail[l]))
                        print("**存款余额不足，%s万元\n" % (cunkuan-sum(gouwuche_jiage)-gouwuche_jiage_fail[l]))
                    else:
                        print("**%s:%s元，加入购物车失败" % (gouwuche_name_fail[l], gouwuche_jiage_fail[l]))
                        print("**存款余额不足，%s万元\n" % (cunkuan-sum(gouwuche_jiage)-gouwuche_jiage_fail[l]))
                        #print("1失败购物车",gouwuche_name_fail)
                else:
                    gouwuche_jiage_fail.append(jiage[i])
                    gouwuche_name_fail.append(name[i])
                    #print("2失败购物车",gouwuche_name_fail)
                    if s==1 or len(gouwuche_name_fail)==1:
                        if (cunkuan-sum(gouwuche_jiage_fail)-sum(gouwuche_jiage))<0:
                            print("**%s:%s元，加入购物车失败" % (gouwuche_name_fail[s], gouwuche_jiage_fail[s]))
                            print("**存款余额不足，%s万元\n" % (cunkuan-sum(gouwuche_jiage)-gouwuche_jiage_fail[s]))
                        elif cunkuan-sum(gouwuche_jiage)==0:
                            print("**%s:%s元，加入购物车成功" % (gouwuche_name_fail[s], gouwuche_jiage_fail[s]))
                            print("**存款余额不足已继续购物，余额为0\n")
                            gouwuche_jiage.append(gouwuche_jiage_fail[s])
                            gouwuche_name.append(gouwuche_name_fail[s])
                            del gouwuche_name_fail[s]
                            del gouwuche_jiage_fail[s]


                        else:
                            print("**%s:%s元，加入购物车失败" % (gouwuche_name_fail[s], gouwuche_jiage_fail[s]))
                    else:
                        print("**%s:%s元，加入购物车失败" % (gouwuche_name_fail[s], gouwuche_jiage_fail[s]))
                        print("存款余额不足，%s万元\n" % (cunkuan-sum(gouwuche_jiage)-gouwuche_jiage_fail[s]))
                        #print("失败购物车总价",sum(gouwuche_jiage_fail))
                    s+=1
            else:
                print("%s:%s万元，已经加入到购物车\n" % (name[i], jiage[i]))
                gouwuche_name.append(name[i])
                gouwuche_jiage.append(jiage[i])
print("\n======购物车清单=====")
if len(gouwuche_name)==0:
    print("购物车空空如也，您未选购任何商品")
    print("=================================\n###没钱哪里凉快就去哪里呆着去，此处不是你来的地方###\n")
else:
    for j in  range(0,len(gouwuche_jiage)):
        print("--%s------%s---"%(gouwuche_name[j],gouwuche_jiage[j]))
    print("****************\n")
    print("已选商品总价为：%s万元" % sum(gouwuche_jiage), "您的可用余额为：%s万元" % cunkuan,end='\t')
    print("\n=================================")
    #确认购买
    while 1:
        k=input("""\n确认购买输入"OK"，取消购买输入任意键退出程序\n""")
        if k=='OK':
            print("**恭喜您支付成功，您的余额为：%s万元**"%(cunkuan-sum(gouwuche_jiage)),"\n欢迎下次光临")
            print("退出程序。。。。")
            break
        else:
            print("\n您已取消购物，谢谢光临！即将本退出程序")
            break
import os
os.system("pause")