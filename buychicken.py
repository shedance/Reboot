
print("公鸡5文钱一只，\n母鸡3文钱一只，\n小鸡3只一文钱，\n用100文钱买一百只鸡,\n其中公鸡，母鸡，小鸡都必须要有，问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱")
for x in range(1,300):
    for g in range(1,20):
        for m in range(1,33):
            if (x/3+m*3+g*5)==100:
                if (x+m+g)==100:
                    print("xiaoji:%s,muji:%s,gongji:%s"%(x,m,g))

