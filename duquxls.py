import xlrd
import pymysql
import datetime




conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='merci1234',db='financialdata',charset='utf8')
curser= conn.cursor()
curser.execute("drop table if exists toxls")
curser.execute("create table toxls (ID int primary key auto_increment) ")
#curser.excute("select `股票名`,`股票代码`,`总资产收益率`,`销售现金比率`,`财务费用比率`from cwzb")
filename="财务报表"
filepath ="F:\\MerciGo\Reports\\%s.xls"%filename
workbook = xlrd.open_workbook(filepath,'rb')#打开xls文件
sheets = workbook.sheet_names()#xls中的sheet以list方式列出
print("sheets name:",sheets)
worksheet = workbook.sheet_by_name(sheets[0]) #需要读取的sheets[0]
#print(type(worksheet.nrows))
#插入主键ID的值
for k in range(1,worksheet.nrows):
    sql3 = "insert into toxls (ID) VALUES (%s)"%(k)
    print(sql3)
    curser.execute(sql3)
print(worksheet.nrows)
#添加字段，将excel表的第一列添加到数据中作为字段
for i in range(0,worksheet.ncols):
    #row = worksheet.row(i)
    #for j in range(0,worksheet.ncols):
    colname = worksheet.cell_value(0,i)
    print(colname)
        #print(worksheet.cell_value(i,j),'\t',end="")
    sql1 = "ALTER TABLE toxls ADD `%s` char(100) null"%(colname)
    curser.execute(sql1)
    conn.commit()
#设置报表日期字段类型为date
sql5="ALTER table toxls modify `报表日期` date"
curser.execute(sql5)
conn.commit()
for n in range(0,worksheet.ncols):
    colname2 = worksheet.cell_value(0,n)
    for j in range(1,worksheet.nrows):
        col_value = worksheet.cell_value(j,n)
        print(type(col_value))
        if colname2 == "报表日期":
            sql2="update toxls set `%s`='%s' where ID =%s"%(colname2,datetime.date.fromtimestamp((col_value-25569)/0.000011574362151665200),j)
        else:
            sql2 ="update toxls set `%s` ='%s' where ID = %s" %(colname2,col_value,j)
        curser.execute(sql2)
        conn.commit()
        print(sql2)





